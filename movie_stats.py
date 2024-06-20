from movie_storage import list_movies
import statistics
import random

def print_random_movie():
    """Print a random movie and its rating from the database"""
    movies = list_movies()
    if not movies:
        print("No movies available in the database.")
        return
    

def calculate_average_rating(movies):
    """Calculate the average rating of the movies"""

    ratings = [movie["Rating"] for movie in movies]

    if not ratings:
        return None
    return sum(ratings) / len(ratings)


def calculate_median_rating(movies):
    """Calculate the median rating of the movie"""
    ratings = sorted([movie["Rating"] for movie in movies])
    if not ratings:
        return None

    return statistics.median(ratings)


def find_best_movies(movies):
    """Find the movie(s) with the highest rating."""
    if not movies:
        return []

    max_rating = max(movie["Rating"] for movie in movies)
    return [movie for movie in movies if movie["Rating"] == max_rating]


def find_worst_movies(movies):
    """Find the movie(s) with the lowest rating."""
    if not movies:
        return []
    min_rating = min(movie["Rating"] for movie in movies)
    return [movie for movie in movies if movie["Rating"] == min_rating]


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


def stats():
    """Print statistics about the movies in the database"""
    movies = list_movies()

    if not movies:
        print("No movies available to display statistics.")
        return

    average_rating = calculate_average_rating(movies)
    median_rating = calculate_median_rating(movies)
    best_movies = find_best_movies(movies)
    worst_movies = find_worst_movies(movies)

    print_stats(average_rating, median_rating, best_movies, worst_movies, len(movies))


