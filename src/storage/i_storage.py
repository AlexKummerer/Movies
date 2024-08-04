"""
Interface for storage classes handling movie data.
"""

from abc import ABC, abstractmethod
from typing import Dict
from src.app.movie_details import MovieDetails
from src.app.movie_utils import MovieData


class IStorage(ABC):
    """
    Interface for storage classes handling movie data.
    """

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
        raise NotImplementedError

    @abstractmethod
    def add_movie(self, movie: MovieDetails) -> None:
        """
        Add a new movie to the storage.

        Args:
            movie (MovieDetails): The movie details to add.

        Raises:
            ValueError: If the movie already exists in the storage.
            KeyError: If there was an error adding the movie to the storage.
        """
        raise NotImplementedError

    @abstractmethod
    def delete_movie(self, title: str) -> None:
        """
        Delete a movie from the storage.

        Args:
            title (str): The title of the movie to delete.

        Raises:
            KeyError: If there was an error deleting the movie from the storage.
        """
        raise NotImplementedError

    @abstractmethod
    def update_movie(self, title: str, notes: str) -> None:
        """
        Update the rating of a movie in the storage.

        Args:
            title (str): The title of the movie to update.
            notes (str): The notes of the movie.

        Raises:
            KeyError: If there was an error updating the movie in the storage.
        """
        raise NotImplementedError

    @abstractmethod
    def generate_website(self) -> None:
        """
        Generate the movie website.
        """
        raise NotImplementedError
