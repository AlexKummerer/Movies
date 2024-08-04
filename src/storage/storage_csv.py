"""
Module for handling CSV storage of movie data.

Returns:
    _type_: A class for handling CSV storage of movie data.
"""

import csv
import logging

from typing import Dict
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
