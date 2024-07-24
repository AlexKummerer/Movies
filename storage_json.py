import json
import os
from typing import Dict
from IStorage import IStorage
from movie_utils import MovieData


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        self.movies = self.load_movies()

    def load_movies(self) ->  Dict[str, Dict[str, MovieData]]:
        """
        Load movies from the JSON file.
 s
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
            raise FileNotFoundError(f"File '{self.file_path}' doesn't exist.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError(f"Error decoding JSON data in file '{self.file_path}'.")

    def save_movies(self) -> None:
        """
        Save the given list of movies to the JSON file.
        """
        try:
            with open(self.file_path, "w") as file:
                json.dump(self.movies, file, indent=4)

        except Exception as e:
            print(f"Error saving movies: {e}")

    def add_movie(self, title: str, year: int, rating: float, poster: str) -> None:
        """
        Add a new movie to the movies database.

        Args:
            title (str):  The title of the movie.
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
            print(f"Movie '{title}' successfully added.")
        except Exception as e:
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
            print(f"Movie '{title}' deleted.")
        else:
            raise KeyError(f"Movie '{title}' doesn't exist.")

    def update_movie(self, title: str, rating: float) -> None:
        """
        Update the rating of a movie in the movies database.

        Args:
            title (str):  The title of the movie to update.
            rating (float): The new rating of the movie.

        Raises:
            KeyError: If the movie doesn't exist in the database.
        """
        if title in self.movies:
            self.movies[title]["Rating"] = rating
            self.save_movies()
            print(f"Movie '{title}' updated with new rating {rating}.")
        else:
            raise KeyError(f"Movie '{title}' doesn't exist.")
