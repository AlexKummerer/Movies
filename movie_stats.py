import statistics
import random
from typing import Any, Dict, List


def print_random_movie(movies: Dict[str, Dict[str, Any]]) -> None:
    """Print a random movie and its rating from the database."""
    if not movies:
        print("No movies available in the database.")
        return
    random_movie_title = random.choice(list(movies.keys()))
    random_movie = movies[random_movie_title]

    print("\nRandom Movie:")
    print(f"Title: {random_movie['Title']}")
    print(f"Rating: {random_movie['Rating']}")


def sort_by_rating(movies: Dict[str, Dict[str, Any]]):
    """
    Sort movies by their rating in descending order and print the sorted list.
    """
    print(movies)
    if not movies:
        print("No movies available to sort.")
        return
    sorted_movies = sorted(movies.values(), key=lambda movie: movie.get("Rating", 0 ), reverse=True)
    print("\nMovies sorted by rating (highest to lowest):")
    for movie in sorted_movies:
        print(
            f"Title: {movie['Title']}, Year: {movie['Year']}, Rating: {movie['Rating']}"
        )


def sort_by_year(movies: Dict[str, Dict[str, Any]]):
    """
    Sort movies by their release year in descending order and print the sorted list.
    """

    if not movies:
        print("No movies available to sort.")
        return

    # Sort the movies by their release year in descending order
    sorted_movies = sorted(movies.values(), key=lambda movie: movie["Year"], reverse=True)

    print("\nMovies sorted by year (newest to oldest):")
    for movie in sorted_movies:
        print(
            f"Title: {movie['Title']}, Year: {movie['Year']}, Rating: {movie['Rating']}"
        )


def calculate_average_rating(movies):
    print(movies)
    ratings = [movie["Rating"] for movie in movies if "Rating" in movie]
    if not ratings:
        return None
    return sum(ratings) / len(ratings)


def calculate_median_rating(movies):
    """Calculate the median rating of the movie"""
    ratings = sorted([movie["Rating"] for movie in movies if "Rating" in movie])
    if not ratings:
        return None
    return statistics.median(ratings)


def find_best_movies(movies: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Find the movie(s) with the highest rating."""
    if not movies:
        return []
    max_rating = max(
        (movie.get("Rating", 0) for movie in movies.values()), default=None
    )
    return [movie for movie in movies.values() if movie.get("Rating") == max_rating]


def find_worst_movies(movies: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Find the movie(s) with the lowest rating."""
    if not movies:
        return []
    min_rating = min(
        (movie.get("Rating", 0) for movie in movies.values()), default=None
    )
    return [movie for movie in movies.values() if movie.get("Rating") == min_rating]


def print_stats(average_rating, median_rating, best_movies, worst_movies, total_movies):
    """Print the statistics about the movies."""
    print(f"\nStatistics for {total_movies} movies in the database:")
    if average_rating is not None:
        print(f"Average rating: {average_rating:.2f}")
    if median_rating is not None:
        print(f"Median rating: {median_rating:.2f}")

    print("\nBest movie(s) by rating:")
    for movie in best_movies:
        print(f"{movie['Title']} ({movie['Year']}): {movie['Rating']}")

    print("\nWorst movie(s) by rating:")
    for movie in worst_movies:
        print(f"{movie['Title']} ({movie['Year']}): {movie['Rating']}")


def stats(movies):
    """Print statistics about the movies in the database"""
    if not movies:
        print("No movies available to display statistics.")
        return
    average_rating = calculate_average_rating(movies)
    median_rating = calculate_median_rating(movies)
    best_movies = find_best_movies(movies)
    worst_movies = find_worst_movies(movies)

    print_stats(average_rating, median_rating, best_movies, worst_movies, len(movies))
