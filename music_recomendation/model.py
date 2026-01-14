import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("music.csv")
df.columns = df.columns.str.strip().str.lower()

features = df[['tempo', 'energy', 'danceability']]
similarity = cosine_similarity(features)

def recommend(song_name):
    if song_name not in df['track_name'].values:
        return ["Song not found"]

    idx = df[df['track_name'] == song_name].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    return [df.iloc[i[0]]['track_name'] for i in scores[1:4]]

