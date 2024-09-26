import pandas as pd
import streamlit as st
# Import necessary functions from visualizations.py
from visualizations import (
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

# Create a title for the dashboard
st.title("Amazon Prime Video Analysis Dashboard")

# Create two columns for side-by-side plots
col1, col2 = st.columns(2)

# Plot in the first column
with col1:
    st.subheader("Number of Movies vs TV Shows")
    fig1 = plot_movies_vs_tvshows(data)
    st.pyplot(fig1)

# Plot in the second column
with col2:
    st.subheader("Distribution of Ratings")
    fig2 = plot_distribution_of_ratings(data)
    st.pyplot(fig2)


