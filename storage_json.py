import json
import os
from IStorage import IStorage




class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        self.movies = self.load_movies()

    def load_movies(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except (IOError, json.JSONDecodeError):
            return {}

    def list_movies(self) -> dict[dict] :
        print(f"\n{len(self.movies)} movies in total\n")
        print(self.movies.items())
        for movie, details in self.movies.items():
            print(f"{movie} ({details['Year']}): {details['Rating']}")


    def save_movies(self) -> None:
        """
        Save the given list of movies to the JSON file.
        """
        try:
            with open(self.file_path, "w") as file:
                json.dump(self.movies, file, indent=4)
                   
        except Exception as e:
            print(f"Error saving movies: {e}")



    def add_movie(self, title, year, rating, poster):
        if title in self.movies:
            raise ValueError(f"Movie '{title}' already exists.")
        new_movie = {"Title": title, "Year": year, "Rating": rating, "Poster": poster}
        self.movies[title] = new_movie

        try:
            self.save_movies()
            print(f"Movie '{title}' successfully added.")
        except Exception as e:
            print(f"Error adding the movie '{title}': {e}")

    def delete_movie(self, title):
        """
        Delete a movie from the movies database.
        """
        if title in self.movies:
            del self.movies[title]
            self.save_movies( )
            print(f"Movie '{title}' deleted.")
        else:
            print(f"Movie '{title}' doesn't e.")


    def update_movie(self, title, rating):
        if title in self.movies:
            self.movies[title]["Rating"] = rating
            self.save_movies()
            print(f"Movie '{title}' updated with new rating {rating}.")
        else:
            print(f"No movie found with the title '{title}'.")