from abc import ABC, abstractmethod
from typing import Dict

from movie_utils import MovieData


class IStorage(ABC):
    @abstractmethod
    def load_movies_file(self) -> Dict[str, Dict[str, MovieData]]: 
        """
        Load movies from the storage.

        Returns:
            Dict[str, Dict[str, MovieData]]: A dictionary of movies.

        Raises:
            IOError: If there was an error loading the movies from the storage.
            json.JSONDecodeError: If there was an error decoding the JSON data.
        """
        pass

    @abstractmethod
    def add_movie(self, title: str, year: int, rating: float, poster: str) -> None:
        """
        Add a new movie to the storage

        Args:
            title (str):  The title of the movie.
            year (int):  The year the movie was released.
            rating (float): The rating of the movie.
            poster (str): The URL of the movie poster.

        Raises:
            ValueError: If the movie already exists in the storage.
            KeyError: If there was an error adding the movie to the storage
        """
        pass

    @abstractmethod
    def delete_movie(self, title: str) -> None:
        """
        Delete a movie from the storage

        Args:
            title (str): The title of the movie to delete.

        Raises:
            KeyError: If there was an error deleting the movie from the storage.
        """
        pass

    @abstractmethod
    def update_movie(self, title: str, rating: float) -> None:
        """
        Update the rating of a movie in the storage

        Args:
            title (str):  The title of the movie to update.
            rating (float):  The new rating of the movie.

        Raises:
            KeyError: If there was an error updating the movie in the storage.
        """
        pass
