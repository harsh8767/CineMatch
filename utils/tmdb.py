import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

API_KEY = st.secrets.get("TMDB_API_KEY") or os.getenv("TMDB_API_KEY")

BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"


@st.cache_data(show_spinner=False)
def fetch_movie_details(movie_id):

    url = (
        f"{BASE_URL}/movie/{movie_id}"
        f"?api_key={API_KEY}"
        f"&append_to_response=credits,videos"
    )

    try:

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        # Already included because of append_to_response
        credits = data.get("credits", {})
        videos = data.get("videos", {})

        # ---------------- Trailer ----------------

        trailer = None

        for video in videos.get("results", []):

            if (
                video.get("site") == "YouTube"
                and video.get("type") == "Trailer"
            ):
                trailer = (
                    f"https://www.youtube.com/watch?v={video['key']}"
                )
                break

        # ---------------- Director ----------------

        director = "N/A"

        for crew in credits.get("crew", []):

            if crew.get("job") == "Director":
                director = crew.get("name")
                break

        # ---------------- Cast ----------------

        cast = [
            actor.get("name")
            for actor in credits.get("cast", [])[:5]
        ]

        # ---------------- Return ----------------

        return {

            "poster": (
                IMAGE_BASE_URL + data["poster_path"]
                if data.get("poster_path")
                else None
            ),

            "rating": data.get("vote_average"),

            "release_date": data.get("release_date"),

            "runtime": data.get("runtime"),

            "overview": data.get("overview"),

            "genres": [
                genre["name"]
                for genre in data.get("genres", [])
            ],

            "director": director,

            "cast": cast,

            "trailer": trailer,

            "tmdb_url": (
                f"https://www.themoviedb.org/movie/{movie_id}"
            ),

            "language": data.get(
                "original_language",
                ""
            ).upper(),

            "status": data.get("status"),

            "budget": data.get("budget"),

            "revenue": data.get("revenue"),
        }

    except requests.exceptions.RequestException:

        return None
