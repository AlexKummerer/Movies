import json
import os
from typing import Dict
from src.storage.IStorage import IStorage
from src.app.movie_utils import MovieData
import requests
from src.config import Config
import logging

logging.basicConfig(level=logging.DEBUG if Config.DEBUG else logging.INFO)
logger = logging.getLogger(__name__)


class JsonStorage(IStorage):
    def __init__(self, file_path: str = Config.DATABASE_URL) -> None:
        """
        Initialize the JsonStorage object with the file path.

        Args:
            file_path (str): File path to the JSON file.
        """
        self.file_path = file_path
        self.movies = self.load_movies_file()

    def load_movies_file(self) -> Dict[str, Dict[str, MovieData]]:
        """
        Load movies from the JSON file.

        Returns:
            Dict[str, Dict[str, MovieData]]: A dictionary of movies.

        Raises:
            FileNotFoundError: If the file doesn't exist.
            json.JSONDecodeError: If there was an error decoding the JSON data.
        """
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            logger.error(f"File '{self.file_path}' doesn't exist.")
            raise
        except json.JSONDecodeError:
            logger.error(f"Error decoding JSON data in file '{self.file_path}'.")
            raise

    def load_movies_api(self, user_search: str) -> Dict[str, MovieData]:
        api_url = f"https://www.omdbapi.com/?apikey={Config.SECRET_KEY}&t={user_search}"
        response = requests.get(api_url)
        if response.status_code == 200:
            movie_data = response.json()
            return {
                "Title": movie_data["Title"],
                "Year": movie_data["Year"],
                "Rating": float(movie_data["imdbRating"]),
                "Poster": movie_data["Poster"],
                "Notes": "",
                "ImdbID": movie_data["imdbID"],
            }
        else:
            logger.error(f"Error: {response.status_code} {response.text}")
            raise requests.RequestException(
                f"Error: {response.status_code} {response.text}"
            )

    def save_movies(self) -> None:
        """
        Save the movies to the JSON file.
        """
        try:
            with open(self.file_path, "w") as file:
                json.dump(self.movies, file, indent=4)
            logger.info(f"Movies successfully saved to '{self.file_path}'.")
        except Exception as e:
            logger.error(f"Error saving movies: {e}")
            raise

    def add_movie(self, title: str, year: int, rating: float, poster: str) -> None:
        """
        Add a new movie to the movies database.

        Args:
            title (str): The title of the movie.
            year (int): The year the movie was released.
            rating (float): The rating of the movie.
            poster (str): The URL of the movie poster.

        Raises:
            ValueError: If the movie already exists in the database.
            KeyError: If there was an error adding the movie to the database.
        """
        if title in self.movies:
            raise ValueError(f"Movie '{title}' already exists.")
        new_movie = {"Title": title, "Year": year, "Rating": rating, "Poster": poster}
        self.movies[title] = new_movie

        try:
            self.save_movies()
            logger.info(f"Movie '{title}' successfully added.")
        except Exception as e:
            logger.error(f"Error adding the movie '{title}': {e}")
            raise KeyError(f"Error adding the movie '{title}': {e}")

    def delete_movie(self, title: str) -> None:
        """
        Delete a movie from the movies database.

        Args:
            title (str): The title of the movie to delete.

        Raises:
            KeyError: If the movie doesn't exist in the database.
        """
        if title in self.movies:
            del self.movies[title]
            self.save_movies()
            logger.info(f"Movie '{title}' successfully deleted.")
        else:
            logger.error(f"Movie '{title}' doesn't exist.")
            raise KeyError(f"Movie '{title}' doesn't exist.")

    def update_movie(self, title: str, notes: str) -> None:
        """
        Update the rating of a movie in the movies database.

        Args:
            title (str): The title of the movie to update.
            notes (str): The notes of the movie.

        Raises:
            KeyError: If there was an error updating the movie in the database.
        """
        if title in self.movies:
            self.movies[title]["Notes"] = notes
            self.save_movies()
            logger.info(f"Movie '{title}' successfully updated.")
        else:
            logger.error(f"Movie '{title}' doesn't exist.")
            raise KeyError(f"Movie '{title}' doesn't exist.")

    def generate_website(self) -> None:
        """
        Generate the movie website.
        """
        movies_html = ""
        for movie in self.movies.values():

            movies_html += (
                f'<li class="movie">'
                f'<a href="https://www.imdb.com/title/{movie["ImdbID"]}" target="_blank">'
                f'<img src="{movie["Poster"]}" class="movie-poster" alt="{movie["Title"]} Poster"/>'
                f"</a>"
                f'<div class="movie-title">{movie["Title"]}</div>'
                f'<p class="movie-year">{movie["Year"]}</p>'
                f'<p class="movie-rating">Rating: {movie["Rating"]}</p>'
                f'<p class="movie-notes">{movie["Notes"]}</p>'
                f"</li>"
            )
        try:
            template_path = os.path.join(Config.TEMPLATE_PATH, "movies_template.html")
            with open(template_path, "r") as file:
                html_content = file.read()

            updated_html_content = html_content.replace(
                "__TEMPLATE_TITLE__", "My Movie App"
            ).replace("__TEMPLATE_MOVIE_GRID__", movies_html)

            output_path = os.path.join(Config.TEMPLATE_PATH, "movie_app.html")
            with open(output_path, "w") as file:
                file.write(updated_html_content)

            logger.info("Website successfully generated.")
        except Exception as e:
            logger.error(f"Error generating website: {e}")
            raise
