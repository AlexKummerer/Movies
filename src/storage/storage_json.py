"""
Module for handling JSON storage of movie data.
"""

import logging
import json
from typing import Dict
from src.storage.base_storage import BaseStorage
from src.app.movie_utils import MovieData

logger = logging.getLogger(__name__)


class JsonStorage(BaseStorage):
    """
    Class for handling JSON storage of movie data.
    """

    def load_movies_file(self) -> Dict[str, Dict[str, MovieData]]:
        """
        Load movies from the JSON file.

        Returns:
            Dict[str, Dict[str, MovieData]]: A dictionary of movies.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            logger.error("File '%s' doesn't exist.", self.file_path)
            raise
        except json.JSONDecodeError:
            logger.error("Error decoding JSON data in file '%s'.", self.file_path)
            raise
        
        

    def save_movies(self) -> None:
        """
        Save movies to the JSON file.
        """
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(self.movies, file, indent=4)
            logger.info("Movies successfully saved to '%s'.", self.file_path)
        except Exception as e:
            logger.error("Error saving movies: %s", e)
            raise
