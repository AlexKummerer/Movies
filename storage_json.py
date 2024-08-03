import json
import os
from typing import Dict
from IStorage import IStorage
from movie_utils import MovieData
from dotenv import load_dotenv
import requests


load_dotenv()
database_url = os.getenv("DATABASE_URL")
secret_key = os.getenv("SECRET_KEY")
debug_mode = os.getenv("DEBUG")


class StorageJson(IStorage):
    def __init__(self, file_path) -> None:
        """
        Initialize the StorageJson object with the file path and API key.

        Args:
            file_path (_type_): File path to the JSON file.
        """
        self.file_path = file_path
        self.movies = self.load_movies_file()

    def load_movies_file(self) -> Dict[str, Dict[str, MovieData]]:
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
            raise json.JSONDecodeError(
                f"Error decoding JSON data in file '{self.file_path}'."
            )

    def load_movies_api(self, user_search: str) -> Dict[str, Dict[str, MovieData]]:

        api_url = f"https://www.omdbapi.com/?apikey={secret_key}&t={user_search}"
        response = requests.get(api_url)
        movie_data = response.json()
        if response.status_code == requests.codes.ok:
            return movie_data
        else:
            print("Error:", response.status_code, response.text)
            return []

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

    def serialize_movie_data(self, movie_title, movie_rating, movie_year, movie_poster):
        output = '<li class="movie">\n'
        output += f'<img src="{movie_poster}" class="movie-poster" alt="{movie_title} Poster"/>\n'
        output += f'<div class="movie-title">{movie_title}</div>\n'
        output += f'<p class="movie-year">{movie_year}</p>\n'
        output += f'<p class="movie-rating">Rating: {movie_rating}</p>\n'
        output += "</li>\n"
        return output

    def generate_website(self):
        movie_data = self.load_movies_file()

        movies_html = ""
        for movie, details in movie_data.items():
            movie_title = movie
            movie_rating = float(details["Rating"])
            movie_year = int(details["Year"])
            movie_poster = str(details["Poster"])
            movies_html += self.serialize_movie_data(
                movie_title, movie_rating, movie_year, movie_poster
            )

        with open("_static/movies_template.html", "r") as file:
            html_content = file.read()

        updated_html_content = html_content.replace(
            "__TEMPLATE_TITLE__", "My Movie App"
        )
        updated_html_content = updated_html_content.replace(
            "__TEMPLATE_MOVIE_GRID__", movies_html
        )

        with open("_static/movie_app.html", "w") as file:
            file.write(updated_html_content)
