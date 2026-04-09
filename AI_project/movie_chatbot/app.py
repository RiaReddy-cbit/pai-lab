from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)   # ✅ MUST be before @app.route

data = pd.read_csv("movies.csv")

data['Genre'] = data['Genre'].str.lower()
data['Director'] = data['Director'].str.lower()
data['Cast'] = data['Cast'].str.lower()

def recommend_movies(genre, director, cast, rating):
    filtered = data

    if genre:
        filtered = filtered[filtered['Genre'].str.contains(genre.lower(), na=False)]

    if director:
        filtered = filtered[filtered['Director'].str.contains(director.lower(), na=False)]

    if cast:
        filtered = filtered[filtered['Cast'].str.contains(cast.lower(), na=False)]

    if rating:
        filtered = filtered[filtered['Rating'] >= float(rating)]

    filtered = filtered.sort_values(by='Rating', ascending=False)

    return filtered.head(5)

@app.route('/', methods=['GET', 'POST'])
def index():
    movies = None

    genres = sorted(data['Genre'].dropna().unique())
    directors = sorted(data['Director'].dropna().unique())
    casts = sorted(data['Cast'].dropna().unique())
    ratings = sorted(data['Rating'].dropna().unique())

    if request.method == 'POST':
        genre = request.form.get('genre', '')
        director = request.form.get('director', '')
        cast = request.form.get('cast', '')
        rating = request.form.get('rating', '')

        movies = recommend_movies(genre, director, cast, rating)

    return render_template(
        'index.html',
        movies=movies,
        genres=genres,
        directors=directors,
        casts=casts,
        ratings=ratings
    )

if __name__ == '__main__':
    app.run(debug=True)
