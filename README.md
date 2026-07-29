# 🎬 CineMatch

> An AI-powered content-based Movie Recommendation System built using Machine Learning, Streamlit, and the TMDB API.

---

## 📌 Overview

CineMatch recommends movies based on their content using cosine similarity. Simply search for a movie, and CineMatch suggests similar movies with posters, ratings, genres, runtime, director, language, and more.

---

## ✨ Features

- 🎥 Content-Based Movie Recommendation
- 🔍 Search from 4,800+ Movies
- 🖼️ Movie Posters from TMDB
- ⭐ IMDb-style Ratings
- 🎭 Genres
- 🎬 Director Information
- 👥 Top Cast
- 🌐 Original Language
- ⏱ Runtime
- 📅 Release Year
- 📝 Movie Overview
- 🎨 Modern Streamlit UI
- ⚡ Fast Recommendations using Cosine Similarity

---

## 🛠 Tech Stack

- Python
- Pandas
- Scikit-learn
- Streamlit
- TMDB API
- Pickle

---

## 📂 Project Structure

```
CineMatch/
│
├── app.py
├── assets/
│   ├── styles.css
│   └── no_poster_avail.jpg
│
├── data/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── models/
│   ├── movies.pkl
│   └── similarity.pkl
│
├── notebook/
│   └── CineMatch.ipynb
│
├── utils/
│   └── tmdb.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/harsh8767/CineMatch.git
```

Go into the project

```bash
cd CineMatch
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
TMDB_API_KEY=your_tmdb_api_key
```

Run the app

```bash
streamlit run app.py
```

---

## 🧠 Machine Learning Workflow

1. Load Movie Dataset
2. Data Cleaning
3. Feature Engineering
4. Tags Generation
5. Text Vectorization
6. Cosine Similarity
7. Save Model using Pickle
8. Streamlit Deployment

---

## 📊 Dataset

- TMDB 5000 Movies Dataset
- TMDB 5000 Credits Dataset

---

## 📸 Screenshots

> Screenshots will be added soon.

---

## 🌟 Future Improvements

- Movie Trailers
- Similar TV Shows
- User Authentication
- Favorite Movies
- Watchlist
- Collaborative Filtering
- Hybrid Recommendation System

---

## 👨‍💻 Developer

**Harsh Chavan**

Computer Engineering Graduate

GitHub: https://github.com/harsh8767

---

## 📜 License

This project is licensed under the MIT License.