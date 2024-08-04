# src/storage/storage_json.py

import json
from typing import Dict
from storage.base_storage import BaseStorage
from src.app.movie_utils import MovieData
import logging

logger = logging.getLogger(__name__)

class JsonStorage(BaseStorage):
    def load_movies_file(self) -> Dict[str, Dict[str, MovieData]]:
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            logger.error(f"File '{self.file_path}' doesn't exist.")
            raise
        except json.JSONDecodeError:
            logger.error(f"Error decoding JSON data in file '{self.file_path}'.")
            raise

    def save_movies(self) -> None:
        try:
            with open(self.file_path, "w") as file:
                json.dump(self.movies, file, indent=4)
            logger.info(f"Movies successfully saved to '{self.file_path}'.")
        except Exception as e:
            logger.error(f"Error saving movies: {e}")
            raise
