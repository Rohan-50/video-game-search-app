from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import os

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://admin:{os.environ['MYSQL_PASSWORD']}@database-1.cbcgy4aq8qap.us-east-2.rds.amazonaws.com/video_game_data"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

with app.app_context():
    try:
        connection = db.engine.connect()
        query = "SELECT 1"
        result = connection.execute(text(query))
        print("Database connection successful!")
    except Exception as e:
        print(f"Error connecting to the database: {e}")


class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    platforms = db.Column(db.JSON)
    stores = db.Column(db.JSON)
    released = db.Column(db.Date)
    background_image = db.Column(db.String(255))
    rating = db.Column(db.Float)
    rating_top = db.Column(db.Integer)
    ratings = db.Column(db.JSON)
    ratings_count = db.Column(db.Integer)
    reviews_text_count = db.Column(db.Integer)
    added = db.Column(db.Integer)
    added_by_status = db.Column(db.JSON)
    metacritic = db.Column(db.Integer)
    updated = db.Column(db.TIMESTAMP)
    tags = db.Column(db.JSON)
    esrb_rating = db.Column(db.JSON)
    reviews_count = db.Column(db.Integer)
    saturated_color = db.Column(db.String(6))
    dominant_color = db.Column(db.String(6))
    short_screenshots = db.Column(db.JSON)
    genres = db.Column(db.JSON)
    name_original = db.Column(db.String(255))
    description = db.Column(db.Text)
    metacritic_platforms = db.Column(db.JSON)
    background_image_additional = db.Column(db.String(255))
    website = db.Column(db.String(255))
    reactions = db.Column(db.JSON)
    reddit_url = db.Column(db.String(255))
    metacritic_url = db.Column(db.String(255))
    developers = db.Column(db.JSON)
    publishers = db.Column(db.JSON)


@app.route('/api/games')
def get_games():
    games = Games.query.all()
    game_list = []

    for game in games:
        game_data = {
            'id': game.id,
            'name': game.name,
            'platforms': game.platforms,
            'stores': game.stores,
            'released': game.released.isoformat() if game.released else None,
            'background_image': game.background_image,
            'rating': game.rating,
            'rating_top': game.rating_top,
            'ratings': game.ratings,
            'ratings_count': game.ratings_count,
            'reviews_text_count': game.reviews_text_count,
            'added': game.added,
            'added_by_status': game.added_by_status,
            'metacritic': game.metacritic,
            'updated': game.updated.isoformat() if game.updated else None,
            'tags': game.tags,
            'esrb_rating': game.esrb_rating,
            'reviews_count': game.reviews_count,
            'saturated_color': game.saturated_color,
            'dominant_color': game.dominant_color,
            'short_screenshots': game.short_screenshots,
            'genres': game.genres,
            'name_original': game.name_original,
            'description': game.description,
            'metacritic_platforms': game.metacritic_platforms,
            'background_image_additional': game.background_image_additional,
            'website': game.website,
            'reactions': game.reactions,
            'reddit_url': game.reddit_url,
            'metacritic_url': game.metacritic_url,
            'developers': game.developers,
            'publishers': game.publishers,
        }
        game_list.append(game_data)

    return jsonify(games=game_list)


if __name__ == '__main__':
    db.create_all()
