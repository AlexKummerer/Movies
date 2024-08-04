"""
Module for handling base storage functionality for movie data.
"""

import os
import logging
from typing import Dict
import requests
from src.storage.i_storage import IStorage
from src.app.movie_utils import MovieData
from src.config import SECRET_KEY, DEBUG, TEMPLATE_PATH
from src.app.movie_details import MovieDetails


logging.basicConfig(level=logging.DEBUG if DEBUG else logging.INFO)
logger = logging.getLogger(__name__)


class BaseStorage(IStorage):
    """
    Base class for handling storage of movie data.
    """

    def __init__(self, file_path: str) -> None:
        """
        Initialize the storage object with a file path.

        Args:
            file_path (str): The path to the file to load movies from.
        """
        self.file_path = file_path
        self.movies = self.load_movies_file()

    def load_movies_file(self) -> Dict[str, Dict[str, MovieData]]:
        """
        Load movies from a file and return them as a dictionary.

        Raises:
            NotImplementedError: Subclasses should implement this method.

        Returns:
            Dict[str, Dict[str, MovieData]]: A dictionary containing movie information.
        """
        raise NotImplementedError("Subclasses should implement this method")

    def load_movies_api(self, user_search: str) -> Dict[str, MovieData]:
        """
        Load movie data from an API using the user's search query.

        Args:
            user_search (str): The user's search query.

        Raises:
            requests.RequestException: If there is an error with the request.

        Returns:
            Dict[str, MovieData]: A dictionary containing movie information.
        """
        api_url = f"https://www.omdbapi.com/?apikey={SECRET_KEY}&t={user_search}"
        response = requests.get(api_url, timeout=10)
        if response.status_code == 200:
            movie_data = response.json()
            rating = movie_data["imdbRating"]
            rating = 0.0 if rating == "N/A" else float(rating)
            return {
                "Title": movie_data["Title"],
                "Year": movie_data["Year"],
                "Rating": rating,
                "Poster": movie_data["Poster"],
                "Notes": "",
                "ImdbID": movie_data["imdbID"],
            }
        logger.error("Error: %d %s", response.status_code, response.text)
        raise requests.RequestException(
            f"Error: {response.status_code} {response.text}"
        )

    def save_movies(self) -> None:
        """
        Save movies to a file.

        Raises:
            NotImplementedError: Subclasses should implement this method.
        """
        raise NotImplementedError("Subclasses should implement this method")

    def add_movie(self, movie: MovieDetails) -> None:
        """
        Add a new movie to the storage.

        Args:
            movie (MovieDetails): The movie details to add.

        Raises:
            ValueError: If the movie already exists.
            KeyError: If there is an error adding the movie.
        """
        if movie.title in self.movies:
            raise ValueError(f"Movie '{movie.title}' already exists.")
        new_movie = {
           "Title": movie.title,
            "Year": movie.year,
            "Rating": movie.rating,
            "Poster": movie.poster,
            "Notes": movie.notes,
            "ImdbID": movie.imdb_id,
        }
        self.movies[movie.title] = new_movie
        try:
            self.save_movies()
            logger.info("Movie '%s' successfully added.", movie.title)
        except Exception as e:
            logger.error("Error adding the movie '%s': %s", movie.title, e)
            raise KeyError(f"Error adding the movie '{movie.title}': {e}") from e


    def delete_movie(self, title: str) -> None:
        """
        Delete a movie from the storage.

        Args:
            title (str): The title of the movie to delete.

        Raises:
            KeyError: If the movie doesn't exist.
        """
        if title in self.movies:
            del self.movies[title]
            self.save_movies()
            logger.info("Movie '%s' successfully deleted.", title)
        else:
            logger.error("Movie '%s' doesn't exist.", title)
            raise KeyError(f"Movie '{title}' doesn't exist.")

    def update_movie(self, title: str, notes: str) -> None:
        """
        Update the notes of a movie in the storage.

        Args:
            title (str): The title of the movie to update.
            notes (str): The new notes for the movie.

        Raises:
            KeyError: If the movie doesn't exist.
        """
        if title in self.movies:
            self.movies[title]["Notes"] = notes
            self.save_movies()
            logger.info("Movie '%s' successfully updated.", title)
        else:
            logger.error("Movie '%s' doesn't exist.", title)
            raise KeyError(f"Movie '{title}' doesn't exist.")

    def generate_website(self) -> None:
        """
        Generate a static HTML website to display the movies.
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
            template_path = os.path.join(TEMPLATE_PATH, "movies_template.html")
            with open(template_path, "r", encoding="utf-8") as file:
                html_content = file.read()

            updated_html_content = html_content.replace(
                "__TEMPLATE_TITLE__", "My Movie App"
            ).replace("__TEMPLATE_MOVIE_GRID__", movies_html)

            output_path = os.path.join(TEMPLATE_PATH, "movie_app.html")
            with open(output_path, "w", encoding="utf-8") as file:
                file.write(updated_html_content)

            logger.info("Website successfully generated.")
        except Exception as e:
            logger.error("Error generating website: %s", e)
            raise
