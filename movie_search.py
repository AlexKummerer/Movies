from typing import Any, Dict


def search_movie(title: str, movies: Dict[str, Dict[str, Any]]) -> None:
    """Search for the movie by given title"""
    searched_movies = [
        movie for movie in movies.values() if title.lower() in movie["Title"].lower()
    ]
    if not searched_movies:
        print(f"No movies found containing '{title}'.")
    else:
        print(f"\nMovies matching '{title}':")
        for movie in searched_movies:
            print(
                f"Title: {movie['Title']}, Year: {movie['Year']}, Rating: {movie['Rating']}"
            )


search_movie("the", {"The Dark Knight": {"Title": "The Dark Knight", "Year": 2008, "Rating": 9.0}})