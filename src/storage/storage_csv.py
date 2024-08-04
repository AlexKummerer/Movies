import csv
from typing import Dict
from storage.base_storage import BaseStorage
from src.app.movie_utils import MovieData
import logging

logger = logging.getLogger(__name__)


class CsvStorage(BaseStorage):
    def load_movies_file(self) -> Dict[str, Dict[str, MovieData]]:
        try:
            with open(self.file_path, mode="r") as file:
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
            logger.error(f"File '{self.file_path}' doesn't exist.")
            raise

    def save_movies(self) -> None:
        try:
            with open(self.file_path, mode="w", newline="") as file:
                fieldnames = ["Title", "Year", "Rating", "Poster", "Notes", "ImdbID"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for movie in self.movies.values():
                    writer.writerow(movie)
            logger.info(f"Movies successfully saved to '{self.file_path}'.")
        except Exception as e:
            logger.error(f"Error saving movies: {e}")
            raise
