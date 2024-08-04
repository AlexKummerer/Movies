"""
Module for handling CSV storage of movie data.

Returns:
    _type_: A class for handling CSV storage of movie data.
"""

import csv
import logging

from typing import Dict
from src.app.movie_details import MovieDetails
from src.storage.base_storage import BaseStorage
from src.app.movie_utils import MovieData

logger = logging.getLogger(__name__)


class CsvStorage(BaseStorage):
    """
    Class for handling CSV storage of movie data.

    Args:
        BaseStorage (_type_):  Base class for handling storage of movie data.
    """

    def load_movies_file(self) -> Dict[str, Dict[str, MovieData]]:
        """
        Load movies from the CSV file

        Returns:
            Dict[str, Dict[str, MovieData]]: A dictionary of movies
        """
        try:
            with open(self.file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                movies = {
                    row["Title"]: {
                        "Title": row["Title"],
                        "Year": int(row["Year"]),
                        "Rating": float(row["Rating"]),
                        "Poster": row["Poster"],
                        "Notes": row.get("Notes", ""),
                        "ImdbID": row["ImdbID"],
                    }
                    for row in reader
                }
            return movies
        except FileNotFoundError:
            logger.error("File %s doesn't exist.", self.file_path)
            raise

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

    def save_movies(self) -> None:
        """
        Save movies to the CSV file
        """
        try:
            with open(self.file_path, mode="w", newline="", encoding="utf-8") as file:
                fieldnames = ["Title", "Year", "Rating", "Poster", "Notes", "ImdbID"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for movie in self.movies.values():
                    writer.writerow(movie)
            logger.info("Movies successfully saved to %s.", self.file_path)
        except Exception as e:
            logger.error("Error saving movies: %e", e)
            raise
