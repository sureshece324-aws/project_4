import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="Amazon Music Clustering",
    layout="wide"
)

st.title("🎵 Amazon Music Song Clustering Dashboard")

# ======================================================
# LOAD DATA
# ======================================================

df = pd.read_csv("Amazon_Music_Final_Categorized.csv")

# =========================================================
# KPI METRICS
# =========================================================

st.header("📊 Dashboard Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Songs", len(df))
col2.metric("Clusters", df['cluster'].nunique())
col3.metric("Genres", df['genres'].nunique())

st.write("Cluster list (0 -Chill/Acoustic, 1 - High-Energy Dance, 2 - Speech-Heavy/Vocal)", unsafe_allow_html=True)


# ======================================================
# CLUSTER DISTRIBUTION
# ======================================================

st.header("🎧 Cluster Distribution")

cluster_counts = df['cluster_name'].value_counts().reset_index()

cluster_counts.columns = ['Cluster', 'Count']

fig_cluster = px.bar(
    cluster_counts,
    x='Cluster',
    y='Count',
    color='Cluster',
    title="Songs per Cluster"
)

st.plotly_chart(fig_cluster, use_container_width=True)

# ======================================================
# FEATURE HEATMAP
# ======================================================

st.header("🔥 Audio Feature Heatmap")

features = [
    'danceability',
    'energy',
    'loudness',
    'speechiness',
    'acousticness',
    'instrumentalness',
    'liveness',
    'valence',
    'tempo'
]

cluster_summary = df.groupby('cluster_name')[features].mean()

fig, ax = plt.subplots(figsize=(12,6))

sns.heatmap(
    cluster_summary,
    annot=True,
    cmap='coolwarm',
    ax=ax
)

st.pyplot(fig)

# ======================================================
# FEATURE DISTRIBUTION
# ======================================================

st.header("📈 Feature Distribution")

selected_feature = st.selectbox(
    "Select Feature",
    features
)

fig_box = px.box(
    df,
    x='cluster_name',
    y=selected_feature,
    color='cluster_name',
    title=f"{selected_feature} Distribution"
)

st.plotly_chart(fig_box, use_container_width=True)

# ======================================================
# TOP TRACKS PER CLUSTER
# ======================================================

st.header("🎵 Top Tracks by Cluster")

selected_cluster = st.selectbox(
    "Select Cluster",
    df['cluster_name'].unique()
)

filtered_df = df[df['cluster_name'] == selected_cluster]

top_tracks = filtered_df[[
    'name_song',
    'name_artists',
    'genres',
    'popularity_songs'
]].sort_values(
    by='popularity_songs',
    ascending=False
).head(10)

st.dataframe(top_tracks)

# ======================================================
# SEARCH SONG
# ======================================================

st.header("🔍 Search Song")

song_search = st.text_input("Enter Song Name")

if song_search:

    results = df[
        df['name_song']
        .str.contains(song_search, case=False, na=False)
    ][[
        'name_song',
        'name_artists',
        'genres',
        'cluster_name'
    ]]

    st.dataframe(results)

# ======================================================
# FOOTER
# ======================================================

st.markdown("---")

