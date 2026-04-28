import streamlit as st
import pandas as pd
import plotly.express as px
from app.utils import load_data, filter_data

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Climate Dashboard", layout="wide")

st.title("🌍 Multi-Country Climate Analysis Dashboard")

# -----------------------------
# LOAD DATA
# -----------------------------
data = load_data()

# -----------------------------
# SIDEBAR CONTROLS
# -----------------------------
st.sidebar.header("Filters")

countries = st.sidebar.multiselect(
    "Select Countries",
    options=data["Country"].unique(),
    default=data["Country"].unique()
)

year_range = st.sidebar.slider(
    "Select Year Range",
    int(data["YEAR"].min()),
    int(data["YEAR"].max()),
    (2015, 2026)
)

variable = st.sidebar.selectbox(
    "Select Variable",
    ["T2M", "T2M_MAX", "T2M_MIN", "PRECTOTCORR", "RH2M", "WS2M"]
)

# -----------------------------
# FILTER DATA
# -----------------------------
filtered = filter_data(data, countries, year_range)

# -----------------------------
# CHART 1: TIME SERIES
# -----------------------------
st.subheader(f"{variable} Trend Over Time")

fig1 = px.line(
    filtered,
    x="YEAR",
    y=variable,
    color="Country",
    title=f"{variable} Comparison Across Countries"
)

st.plotly_chart(fig1, use_container_width=True)

# -----------------------------
# CHART 2: DISTRIBUTION
# -----------------------------
st.subheader("Distribution Comparison")

fig2 = px.box(
    filtered,
    x="Country",
    y=variable,
    color="Country"
)

st.plotly_chart(fig2, use_container_width=True)

# -----------------------------
# SUMMARY STATS
# -----------------------------
st.subheader("Summary Statistics")

st.dataframe(
    filtered.groupby("Country")[variable].agg(["mean", "median", "std"])
)