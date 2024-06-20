import json
import os

FILE_NAME: str = "movies.json"


def list_movies() -> list[dict]:
    """
    The function loads the information from the JSON
    file and returns the data.

    Returns:
        list[dict]: Returns a dictionary of dictionaries that
                    contains the movies information in the database.
    """

    if not os.path.exists(FILE_NAME):
        print(f"No file named {FILE_NAME} found.")
        return []

    with open("movies.json", "r") as file:
        movies = json.load(file)
        if not movies:
            print("no movies found in the file.")
            return []
        return movies


def save_movies(movies: list[dict]):
    """Save movies to the JSON file

    Args:
        movies (list[dict]): movies list to save
    """

    with open(FILE_NAME, "w") as file:
        json.dump(movies, file, indent=4)


def add_movie(title: str, year: int, rating: float) -> None:
    """Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.

    Args:
        title (str): title of the movie
        year (int): year of the movie
        rating (float): rating of the movie
    """
    current_movies: list[dict] = list_movies()
    if not current_movies:
        current_movies = []
    new_movie: dict = {"Title": title, "Year": year, "Rating": rating}
    current_movies.append(new_movie)

    try:
        save_movies(current_movies)
        print(f"Movie {title} succesfully added")
    except Exception as e:
        print(f"There was an error by adding your movie {title}")
        print("Error Message:", e)


def delete_movie(title: str) -> None:
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    movies = list_movies()

    updated_movies = [
        movie for movie in movies if movie["Title"].lower() != title.lower()
    ]
    save_movies(updated_movies)

    print(
        f"\nMovie '{title}' deleted."
        if len(movies) != len(updated_movies)
        else f"\nNo movie found with the title '{title}'."
    )


def get_movie_by_title(title: str) -> dict:
    """get the movie by title

    Args:
        title (str): Title of the movie

    Returns:
        dict: get the information of the film
    """
    movies = list_movies()

    movie = next(
        (movie for movie in movies if movie["Title"].lower() == title.lower()), None
    )

    return movie


def update_movie(title: str, rating: float) -> None:
    """Updates a movie from the movies database

    Args:
        title (str): title of the movie
        rating (float): new rating of the movie
    """

    movies = list_movies()
    for movie in movies:
        if movie["Title"].lower() == title.lower():
            movie["Rating"] = rating
            break
    save_movies(movies)
        
