from flask import Flask, request, jsonify, render_template
from model import recommend

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend_song():
    data = request.get_json()
    song = data.get("song", "")
    result = recommend(song)
    return jsonify({"recommended_songs": result})

if __name__ == "__main__":
    app.run(debug=True)
