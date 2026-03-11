"""
Bollywood Music Recommendation System
-------------------------------------

A simple Streamlit app that recommends similar Bollywood songs based on a
given song name using a precomputed similarity matrix.

Author: <Harsh Kumar>
"""

import streamlit as st
import pickle

df=pickle.load(open('songs_df.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

st.title("Bollywood Music Recommended System")

user_input=st.text_input("Enter a song name:")

def recommend(song):
    song=song.lower()
    try:
        index=df[df['song_name'].str.lower()==song].index[0]
    except:
        return []
    distances=similarity[index]
    song_list=sorted(list(enumerate(distances)),
                     reverse=True,key=lambda x:x[1])[1:6]  
   
    rec=[]
    for i,score in song_list:
       rec.append({
           "song":df.iloc[i]["song_name"],
           "artist":df.iloc[i]["artist"],
           "thumbnail":df.iloc[i]["thumbnail"]if
           "thumbnail" in df.columns else None
       })
    return rec
if st.button("Recommend"):
    try:
        idx=df[df['song_name'].str.lower()==user_input.lower()].index[0]
        st.subheader("You Searched for:")
        col1,col2=st.columns([1,3])
    
        with col1:
            if "thumbnail" in df.columns:
                st.image(df.iloc[idx]["thumbnail"],width=100)
        with col2:
            st.write("**Song Name:**",df.iloc[idx]["song_name"])
            st.write("**Artist:**",df.iloc[idx]["artist"])
    except:   
        st.error("Song not found. Please try another song.")     
        st.stop()

    st.subheader("Recommended Songs:")
    result=recommend(user_input)
    for item in result:
        col1,col2=st.columns([1,3])
        with col1:
            if item["thumbnail"]:
                st.image(item["thumbnail"],width=100)
        with col2:
            st.write("**" + item["song"] + "**")
            st.write(item["artist"])