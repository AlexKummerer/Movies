import json
import os

FILE_NAME: str = "movies.json"


def list_movies() -> list[dict]:
    """
    Load the movies from the JSON file and return them.
    """
    if not os.path.exists(FILE_NAME):
        print(f"No file named {FILE_NAME} found.")
        return []
    try:
        with open(FILE_NAME, "r") as file:
            movies = json.load(file)
            if not movies:
                print("No movies found in the file. s")
            return movies
    except json.JSONDecodeError:
        print("Error reading the movies file. It might be corrupted.")
        return []


def save_movies(movies: list[dict]) -> None:
    """
    Save the given list of movies to the JSON file.
    """
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(movies, file, indent=4)
    except Exception as e:
        print(f"An error occurred while saving movies: {e}")


def add_movie(title: str, year: int, rating: float) -> None:
    """
    Add a new movie to the movies database and save it.
    """
    current_movies = list_movies()
    new_movie = {"Title": title, "Year": year, "Rating": rating}
    current_movies.append(new_movie)
    try:
        save_movies(current_movies)
        print(f"Movie '{title}' successfully added.")
    except Exception as e:
        print(f"Error adding the movie '{title}': {e}")


def delete_movie(title: str) -> None:
    """
    Delete a movie from the movies database.
    """
    movies = list_movies()
    updated_movies = [
        movie for movie in movies if movie["Title"].lower() != title.lower()
    ]
    if len(movies) == len(updated_movies):
        print(f"No movie found with the title '{title}'.")
    else:
        save_movies(updated_movies)
        print(f"Movie '{title}' deleted.")


def get_movie_by_title(title: str) -> dict:
    """
    Get a movie by its title and return.
    """
    movies = list_movies()
    return next(
        (movie for movie in movies if movie["Title"].lower() == title.lower()), None
    )


def update_movie(title: str, rating: float) -> None:
    """
    Update the rating of a movie in the movies database.
    """
    movies = list_movies()
    for movie in movies:
        if movie["Title"].lower() == title.lower():
            movie["Rating"] = rating
            save_movies(movies)
            print(f"Movie '{title}' updated with new rating {rating}.")
            return
    print(f"No movie found with the title '{title}'.")
