import json
import os


def list_movies(filename="movies.json"):
    """
    Returns a dictionary of dictionaries that
    contains the movies information in the database.

    The function loads the information from the JSON
    file and returns the data.

    For example, the function may return:
    {
      "Titanic": {
        "rating": 9,
        "year": 1999
      },
      "..." {
        ...
      },
    }
    or
    {
        "Title": "Inception",
        "Rating": 8.8,
        "Year": 2010,
        "Director": "Christopher Nolan",
        "Genre": "Science Fiction"
    },
    {
        "Title": "The Matrix",
        "Rating": 8.7,
        "Year": 1999,
        "Director": "Lana Wachowski, Lilly Wachowski",
        "Genre": "Action"
    },
    """

    if not os.path.exists(filename):
        print(f"No file named {filename} found.")
        return []

    with open("movies.json", "r") as file:
        movies = json.load(file)
        if not movies:
            print("no movies found in the file.")
            return []
        print(f"{len(movies)} movies in total")
        for movie in movies:
           print(f"{movie['Title']} ({movie['Year']}): {movie['Rating']}")  
        return movies


def add_movie(title, year, rating):
    """
    Adds a movie to the movies database.
    Loads the information from the JSON file, add the movie,
    and saves it. The function doesn't need to validate the input.
    """
    current_movies: list[dict] = list_movies()
    if not current_movies:
        current_movies = []
    new_movie: dict = {"Title": title, "Year": year, "Rating": rating}
    current_movies.append(new_movie)

    movies_json = json.dumps(current_movies, indent=4)

    with open("movies.json", "w") as file:
        file.write(movies_json)


def delete_movie(title):
    """
    Deletes a movie from the movies database.
    Loads the information from the JSON file, deletes the movie,
    and saves it. The function doesn't need to validate the input.
    """
    pass


def update_movie(title, rating):
    """
    Updates a movie from the movies database.
    Loads the information from the JSON file, updates the movie,
    and saves it. The function doesn't need to validate the input.
    """
    pass

