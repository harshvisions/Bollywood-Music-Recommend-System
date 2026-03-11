# Bollywood Music Recommendation System 🎵

A simple **content-based music recommender** that suggests similar Bollywood songs
based on a song you enter. The app is built with **Streamlit** and uses a
precomputed **similarity matrix** over a Bollywood songs dataset.

> 💡 Type a song name and get 5 recommended songs with their artist names
> (and thumbnails if available).

---

## 🚀 Features

- Search for a Bollywood song by name
- View details of the song you searched
- Get top 5 similar song recommendations
- Shows artist name and thumbnail (when available)
- Simple, clean UI using Streamlit

---

## 🧠 How it works (high-level)

1. A dataset of Bollywood songs is preprocessed and stored in `songs_df.pkl`.
2. A similarity matrix (`similarity.pkl`) is computed using song features
   (e.g., lyrics/metadata embeddings, etc.).
3. When you enter a song name, the app:
   - Finds the song in the dataframe
   - Looks up its row in the similarity matrix
   - Sorts other songs by similarity score
   - Returns the top 5 most similar songs

> **Note:** The full dataset (with lyrics) is **not included** in this public repo
> due to copyright. A small sample file (`data/songs_sample.csv`) is provided
> only for demonstration.

---

## 📂 Project Structure
.
├─ app.py                  # Streamlit app
├─ data/
│  └─ songs_sample.csv     # Sample of the Bollywood songs dataset (no lyrics)
├─ models/
│  ├─ songs_df.pkl         # Preprocessed dataframe 
│  └─ similarity.pkl       # Similarity matrix for recommendations
├─ requirements.txt
└─ README.md
