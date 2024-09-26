#This dashboard uses options

import streamlit as st
import pandas as pd
from visualization import (
    plot_movies_vs_tvshows,
    plot_distribution_of_ratings,
    plot_titles_per_year,
    plot_titles_per_decade,
    plot_top_genres,
    plot_genre_distribution,
    plot_genre_distribution_post_2000,
    plot_movie_duration_distribution,
    plot_top_countries,
    plot_top_directors,
    plot_top_actors,
    plot_tv_show_durations,
    plot_movies_by_duration_group
)

# Load your dataset
data = pd.read_csv('amazon_prime_titles.csv')

# Set the title for the dashboard
st.title("Amazon Prime Video Insights Dashboard")

# Add a sidebar for navigation
st.sidebar.header("Navigation")
options = [
    "Movies vs TV Shows",
    "Distribution of Ratings",
    "Titles Released per Year",
    "Titles Released per Decade",
    "Top Genres",
    "Genre Distribution",
    "Genre Distribution (Post 2000)",
    "Movie Duration Distribution",
    "Top Countries",
    "Top Directors",
    "Top Actors",
    "TV Show Durations",
    "Movies by Duration"
]
selection = st.sidebar.selectbox("Select Visualization", options)

# Set a color theme for the dashboard
st.markdown("""
<style>
    .reportview-container {
        background: #f5f5f5;
    }
    .sidebar .sidebar-content {
        background: #ffffff;
    }
</style>
""", unsafe_allow_html=True)

# Define a function to display the selected visualization
def display_visualization(selection):
    if selection == "Movies vs TV Shows":
        st.header("Number of Movies vs TV Shows")
        st.pyplot(plot_movies_vs_tvshows(data))
    elif selection == "Distribution of Ratings":
        st.header("Distribution of Ratings")
        st.pyplot(plot_distribution_of_ratings(data))
    elif selection == "Titles Released per Year":
        st.header("Number of Titles Released Each Year")
        st.pyplot(plot_titles_per_year(data))
    elif selection == "Titles Released per Decade":
        st.header("Number of Titles Released Each Decade")
        st.pyplot(plot_titles_per_decade(data))
    elif selection == "Top Genres":
        st.header("Top 10 Genres on Amazon Prime")
        st.pyplot(plot_top_genres(data))
    elif selection == "Genre Distribution":
        st.header("Distribution of Genres Across Release Years")
        genre_distribution = data['listed_in'].str.get_dummies(sep=', ').groupby(data['release_year']).sum()
        st.pyplot(plot_genre_distribution(genre_distribution))
    elif selection == "Genre Distribution (Post 2000)":
        st.header("Distribution of Genres Across Release Years (2000 and Onwards)")
        st.pyplot(plot_genre_distribution_post_2000(data))
    elif selection == "Movie Duration Distribution":
        st.header("Distribution of Duration for Movies")
        st.pyplot(plot_movie_duration_distribution(data))
    elif selection == "Top Countries":
        st.header("Top 10 Countries by Number of Titles on Amazon Prime")
        st.pyplot(plot_top_countries(data))
    elif selection == "Top Directors":
        st.header("Top 10 Directors by Number of Titles on Amazon Prime")
        st.pyplot(plot_top_directors(data))
    elif selection == "Top Actors":
        st.header("Top 10 Actors on Amazon Prime")
        st.pyplot(plot_top_actors(data))
    elif selection == "TV Show Durations":
        st.header("TV Show Durations")
        st.pyplot(plot_tv_show_durations(data))
    elif selection == "Movies by Duration":
        st.header("Number of Movies by Duration")
        st.pyplot(plot_movies_by_duration_group(data))

# Display the selected visualization
display_visualization(selection)
