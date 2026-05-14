# Project_4 - Amazon_Music_Clustering

**Project Objective**

The goal of this project was to automatically group songs into meaningful clusters using audio characteristics instead of manually assigned genres. Since music platforms contain millions of songs, unsupervised machine learning was used to discover hidden musical patterns and similarities among tracks.

**Data Preprocessing**

The dataset was cleaned and prepared before clustering.

**Steps Performed:**

**Removed unnecessary columns:**

  song IDs, artist IDs, release dates, popularity-related fields etc..

**Checked for:**

  missing values, duplicate records

**Selected important audio features:**

  danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration_ms.

Applied StandardScaler to normalize features because clustering algorithms are distance-based.

**Dimensionality Reduction**

PCA (Principal Component Analysis) was applied for visualization purposes.

This reduced high-dimensional audio features into two principal components, allowing cluster visualization in 2D space while preserving significant variance.

**Clustering Method**

K-Means Clustering was selected as the primary clustering technique.

Cluster Evaluation Techniques:

Elbow Method

Silhouette Score

**Best Result:**

The highest silhouette score was achieved at:

K = 3

Silhouette Score ≈ 0.24

This indicated that three clusters provided the best balance between cluster separation and compactness.

**Cluster Interpretations**

**Cluster 0 — Chill / Acoustic**

  **Characteristics:**

    High acousticness, Lower energy, Softer loudness, Relaxed musical mood

  **Represents:**

    Acoustic songs, Calm listening tracks, Soft indie music

**Cluster 1 — High-Energy Dance**

  **Characteristics:**

    High danceability, High energy, Higher tempo, Positive valence

  **Represents:**

    Party songs, Dance music, Energetic pop tracks

**Cluster 2 — Instrumental / Focus**

  **Characteristics:**

    Higher instrumentalness, Moderate tempo, Lower speechiness

  **Represents:**

    Instrumental music, Focus/study playlists, Ambient tracks

**Visualizations Used**

The following visualizations were created to analyze clustering performance and cluster behavior:

#Elbow Method Plot
#PCA Scatter Plot
#Heatmaps
#Boxplots
#Bar Charts
#Cluster Distribution Charts

These visualizations helped understand how musical properties varied across clusters.

## 📁 Project Structure

```text
Amazon-Music-Clustering/
│
├── Inputdata/
│   └── single_genre_artist.csv
│
├── notebooks/
│   └── Amazon_Music.ipynb
│
├── Outputdata/
│   └── Amazon_Music_Final_Categorized.csv
│
├── streamlit_app/
│   └── app.py
│
├── images/
│   └── visualizations/
│
└── README.md
```
