import pickle
import streamlit as st

from utils.tmdb import fetch_movie_details

# ==========================================================
# CONFIG
# ==========================================================

APP_TITLE = "🎬 CineMatch"
NUM_RECOMMENDATIONS = 5

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="🎬",
    layout="wide",
)

# ==========================================================
# LOAD CSS
# ==========================================================

def load_css():
    with open("assets/styles.css", encoding="utf-8") as css:
        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True,
        )

load_css()

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.title(APP_TITLE)

    st.divider()

    st.subheader("About")

    st.write(
        "CineMatch is a content-based movie recommendation "
        "system powered by Machine Learning and TMDB."
    )

    st.divider()

    st.subheader("Tech Stack")

    st.markdown(
        """
- 🐍 Python
- 📊 Pandas
- 🤖 Scikit-learn
- 🎨 Streamlit
- 🎬 TMDB API
"""
    )

    st.divider()

    st.subheader("Developer")

    st.write("Harsh Chavan")

    st.caption("Computer Engineering Graduate")

# ==========================================================
# HERO
# ==========================================================

st.markdown(
    """
<div class="hero">

<h1>🎬 CineMatch</h1>

<h3>Discover Your Next Favourite Movie</h3>

<p>
AI-powered content-based recommendation system
built using Machine Learning and TMDB.
</p>

</div>
""",
    unsafe_allow_html=True,
)

st.divider()

# ==========================================================
# LOAD MODEL
# ==========================================================

@st.cache_resource
def load_model():

    with open("models/movies.pkl", "rb") as f:
        movies = pickle.load(f)

    with open("models/similarity.pkl", "rb") as f:
        similarity = pickle.load(f)

    return movies, similarity


movies, similarity = load_model()

# ==========================================================
# RECOMMENDATION ENGINE
# ==========================================================

def recommend(movie_name):

    movie_index = movies[
        movies["title"] == movie_name
    ].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True,
    )[1 : NUM_RECOMMENDATIONS + 1]

    recommendations = []

    for movie in movie_list:

        data = movies.iloc[movie[0]]

        recommendations.append(
            {
                "title": data["title"],
                "movie_id": int(data["movie_id"]),
            }
        )

    return recommendations

# ==========================================================
# SEARCH
# ==========================================================

st.markdown("## 🎥 Find Your Movie")

st.caption(
    "Search from over 4,800 movies in our database."
)

selected_movie = st.selectbox(
    "",
    movies["title"].values,
    index=None,
    placeholder="Search or Select a Movie..."
)

recommend_clicked = st.button(
    "🍿 Recommend Movies",
    use_container_width=True
)


# ==========================================================
# MOVIE DETAILS
# ==========================================================

if selected_movie and recommend_clicked:

    selected_movie_id = int(
        movies.loc[
            movies["title"] == selected_movie,
            "movie_id"
        ].iloc[0]
    )

    selected_details = fetch_movie_details(
        selected_movie_id
    )

    left, right = st.columns(
        [1, 2.3],
        gap="large"
    )

    # ------------------------------------------------------
    # POSTER
    # ------------------------------------------------------

    with left:

        if (
            selected_details
            and selected_details.get("poster")
        ):

            st.image(
                selected_details["poster"],
                width=280
            )

        else:

            st.image(
                "assets/no_poster_avail.jpg",
                width=280
            )

    # ------------------------------------------------------
    # DETAILS
    # ------------------------------------------------------

    with right:

        rating = (
            f"{selected_details['rating']:.1f}"
            if selected_details
            and selected_details.get("rating")
            else "N/A"
        )

        year = (
            selected_details["release_date"][:4]
            if selected_details
            and selected_details.get("release_date")
            else "N/A"
        )

        runtime = (
            f"{selected_details['runtime']} min"
            if selected_details
            and selected_details.get("runtime")
            else "N/A"
        )

        genres = (
            " • ".join(selected_details["genres"])
            if selected_details
            and selected_details.get("genres")
            else "N/A"
        )

        director = (
            selected_details.get("director", "N/A")
            if selected_details
            else "N/A"
        )

        language = (
            selected_details.get("language", "N/A")
            if selected_details
            else "N/A"
        )

        cast = (
            ", ".join(
                selected_details.get("cast", [])
            )
            if selected_details
            else "N/A"
        )

        status = (
            selected_details.get("status", "N/A")
            if selected_details
            else "N/A"
        )

        budget = (
            selected_details.get("budget", 0)
            if selected_details
            else 0
        )

        revenue = (
            selected_details.get("revenue", 0)
            if selected_details
            else 0
        )

        st.markdown(
            f"""
<div class="selected-title">
{selected_movie}
</div>
""",
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
<div class="selected-meta">
⭐ {rating}
&nbsp;&nbsp;•&nbsp;&nbsp;
📅 {year}
&nbsp;&nbsp;•&nbsp;&nbsp;
⏱ {runtime}
</div>
""",
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
<div class="selected-genres">
🎭 {genres}
</div>
""",
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
<div class="selected-director">
🎬 <b>Director:</b> {director}
</div>
""",
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
<div class="selected-language">
🌐 <b>Language:</b> {language}
</div>
""",
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
<div class="selected-cast">
👥 <b>Cast:</b> {cast}
</div>
""",
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
<div class="selected-extra">
💰 Budget: ${budget:,}<br>
💵 Revenue: ${revenue:,}<br>
🎞 Status: {status}
</div>
""",
            unsafe_allow_html=True,
        )

        if selected_details.get("overview"):

            st.markdown(
                f"""
<div class="selected-overview">
{selected_details["overview"]}
</div>
""",
                unsafe_allow_html=True,
            )

        if selected_details.get("trailer"):

            st.link_button(
                "▶ Watch Trailer",
                selected_details["trailer"]
            )

        st.link_button(
            "🎬 View on TMDB",
            selected_details["tmdb_url"]
        )

    st.divider()

    st.subheader(
        f"🍿 Because You Watched {selected_movie}"
    )

    recommended_movies = recommend(selected_movie)

        # ==========================================================
    # MOVIE CARD
    # ==========================================================

    def display_movie_card(movie):

        details = fetch_movie_details(movie["movie_id"])

        poster = (
            details.get("poster")
            if details and details.get("poster")
            else None
        )

        rating = (
            f"{details['rating']:.1f}"
            if details
            and details.get("rating")
            else "N/A"
        )

        year = (
            details["release_date"][:4]
            if details
            and details.get("release_date")
            else "N/A"
        )

        genres = (
            " • ".join(details.get("genres", [])[:2])
            if details
            else ""
        )


            # Poster
        if poster:

            st.image(
                poster,
                use_container_width=True
        )

        else:

            st.image(
                "assets/no_poster_avail.jpg",
                use_container_width=True
        )

    # Movie information
        st.markdown(
        f"""
<div class="movie-details">

<div class="movie-title">
{movie['title']}
</div>

<div class="movie-meta">
⭐ {rating} &nbsp;&nbsp;•&nbsp;&nbsp; 📅 {year}
</div>

<div class="movie-genres">
{genres}
</div>

</div>
""",
        unsafe_allow_html=True,
    )

    #     st.markdown(
    #     f"""
    #     <div class="recommendation-card">

    #         <img
    #             src="{poster}"
    #             class="recommendation-poster"
    #         >

    #         <div class="movie-details">

    #             <div class="movie-title">
    #                 {movie['title']}
    #             </div>

    #             <div class="movie-meta">
    #                 ⭐ {rating} &nbsp; • &nbsp; 📅 {year}
    #             </div>

    #             <div class="movie-genres">
    #                 {genres}
    #             </div>

    #         </div>

    #     </div>
    #     """,
    #     unsafe_allow_html=True
    # )

    # ==========================================================
    # FIRST ROW
    # ==========================================================

    row1 = st.columns(
        3,
        gap="large"
    )

    for column, movie in zip(
        row1,
        recommended_movies[:3]
    ):

        with column:

            display_movie_card(movie)

    st.markdown("<br>", unsafe_allow_html=True)

    # ==========================================================
    # SECOND ROW
    # ==========================================================

    left_space, col1, col2, right_space = st.columns(
        [0.25, 1, 1, 0.25],
        gap="large"
    )

    with col1:

        display_movie_card(
            recommended_movies[3]
        )

    with col2:

        display_movie_card(
            recommended_movies[4]
        )

# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.markdown(
    """
<div class="footer">

<h4>🎬 CineMatch</h4>

<p>
Built with ❤️ using Python • Streamlit • Scikit-learn • TMDB API
</p>

<p>
Created by <b>Harsh Chavan</b>
</p>

<p>
© 2026 CineMatch
</p>

</div>
""",
    unsafe_allow_html=True,
)