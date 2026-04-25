import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# streamlit run "/Users/zacharyfalzone/Desktop/SouthernCTUniversity/Spring_2026/Sports_Performance/Mav2011Repo/Mavs2011.py"

# regular season data
df = pd.read_csv('https://raw.githubusercontent.com/zachjf9/Mav2011Repo/refs/heads/main/MavsRegularSeason.csv')

# playoff data
df = pd.read_csv('https://raw.githubusercontent.com/zachjf9/Mav2011Repo/refs/heads/main/MavsPlayOffs.csv')

st.title("Mavs 2011 Season Performance Analysis")



