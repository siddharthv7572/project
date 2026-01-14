import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("music.csv")

# Select important audio features
features = [
    "energy",
    "tempo",
    "danceability",
    "loudness",
    "valence",
    "acousticness",
    "track_popularity"
]

# Remove missing values
df = df.dropna(subset=features)

# Normalize features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(df[features])

# Compute similarity
similarity = cosine_similarity(scaled_features)

def recommend(song_name, n=5):
    if song_name not in df["track_name"].values:
        print("Song not found")
        return

    idx = df[df["track_name"] == song_name].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\nRecommended songs similar to '{song_name}':\n")
    for i in scores[1:n+1]:
        row = df.iloc[i[0]]
        print(f"{row['track_name']} - {row['track_artist']}")

# Test
recommend("Espresso")
