# src/storage/base_storage.py

import json
import csv
from typing import Dict
from src.storage.IStorage import IStorage
from src.app.movie_utils import MovieData
import requests
from src.config import Config
import logging

logging.basicConfig(level=logging.DEBUG if Config.DEBUG else logging.INFO)
logger = logging.getLogger(__name__)

class BaseStorage(IStorage):
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
        self.movies = self.load_movies_file()

    def load_movies_file(self) -> Dict[str, Dict[str, MovieData]]:
        raise NotImplementedError("Subclasses should implement this method")

    def load_movies_api(self, user_search: str) -> Dict[str, MovieData]:
        api_url = f"https://www.omdbapi.com/?apikey={Config.SECRET_KEY}&t={user_search}"
        response = requests.get(api_url)
        if response.status_code == 200:
            movie_data = response.json()
            rating = movie_data["imdbRating"]
            rating = 0.0 if rating == 'N/A' else float(rating)
            return {
                "Title": movie_data["Title"],
                "Year": movie_data["Year"],
                "Rating": rating,
                "Poster": movie_data["Poster"],
                "Notes": "",
                "ImdbID": movie_data["imdbID"]
            }
        else:
            logger.error(f"Error: {response.status_code} {response.text}")
            raise requests.RequestException(f"Error: {response.status_code} {response.text}")

    def save_movies(self) -> None:
        raise NotImplementedError("Subclasses should implement this method")

    def add_movie(self, title: str, year: int, rating: float, poster: str, imdb_id: str) -> None:
        if title in self.movies:
            raise ValueError(f"Movie '{title}' already exists.")
        new_movie = {"Title": title, "Year": year, "Rating": rating, "Poster": poster, "Notes": "", "ImdbID": imdb_id}
        self.movies[title] = new_movie
        try:
            self.save_movies()
            logger.info(f"Movie '{title}' successfully added.")
        except Exception as e:
            logger.error(f"Error adding the movie '{title}': {e}")
            raise KeyError(f"Error adding the movie '{title}': {e}")

    def delete_movie(self, title: str) -> None:
        if title in self.movies:
            del self.movies[title]
            self.save_movies()
            logger.info(f"Movie '{title}' successfully deleted.")
        else:
            logger.error(f"Movie '{title}' doesn't exist.")
            raise KeyError(f"Movie '{title}' doesn't exist.")

    def update_movie(self, title: str, notes: str) -> None:
        if title in self.movies:
            self.movies[title]["Notes"] = notes
            self.save_movies()
            logger.info(f"Movie '{title}' successfully updated.")
        else:
            logger.error(f"Movie '{title}' doesn't exist.")
            raise KeyError(f"Movie '{title}' doesn't exist.")

    def generate_website(self) -> None:
        movies_html = ""
        for movie in self.movies.values():
            movies_html += (
                f'<li class="movie">'
                f'<a href="https://www.imdb.com/title/{movie["ImdbID"]}" target="_blank">'
                f'<img src="{movie["Poster"]}" class="movie-poster" alt="{movie["Title"]} Poster"/>'
                f'</a>'
                f'<div class="movie-title">{movie["Title"]}</div>'
                f'<p class="movie-year">{movie["Year"]}</p>'
                f'<p class="movie-rating">Rating: {movie["Rating"]}</p>'
                f'<p class="movie-notes">{movie["Notes"]}</p>'
                f'</li>'
            )
        try:
            template_path = os.path.join(Config.TEMPLATE_PATH, 'movies_template.html')
            with open(template_path, "r") as file:
                html_content = file.read()

            updated_html_content = html_content.replace(
                "__TEMPLATE_TITLE__", "My Movie App"
            ).replace("__TEMPLATE_MOVIE_GRID__", movies_html)

            output_path = os.path.join(Config.TEMPLATE_PATH, 'movie_app.html')
            with open(output_path, "w") as file:
                file.write(updated_html_content)

            logger.info("Website successfully generated.")
        except Exception as e:
            logger.error(f"Error generating website: {e}")
            raise
