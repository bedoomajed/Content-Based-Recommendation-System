import streamlit as st
import pandas as pd

st.title("AI Movie Recommendation System")
movie_name = st.text_input(
    "Enter Movie Name"
)