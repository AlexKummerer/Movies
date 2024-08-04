from typing import Dict, List, TypedDict
import random


class MovieData(TypedDict):
    Title: str
    Year: int
    Rating: float
    Poster: str
    Notes: str
    ImdbId: str


class MovieUtils:
    """Utility class for movie-related functionalities like filtering, searching, and statistics."""

    def __init__(self, movies: Dict[str, Dict[str, MovieData]]):
        """Initialize the utility class with a list of movies."""
        self.movies = movies

    def filter_movies_by_rating_and_year(
        self, min_rating=0.0, start_year=None, end_year=None
    ) -> List[Dict[str, MovieData]]:
        """Filter movies by rating and optionally by year.

        Args:
            min_rating (float): The minimum rating to filter by.
            start_year (int): The start year to filter by.
            end_year (int): The end year to filter by.

        Returns:
            List[Dict[str, MovieData]]: A list of filtered movies.
        """
        filtered_movies = [
            movie
            for movie in self.movies.values()
            if float(movie.get("Rating", 0)) >= min_rating
            and (start_year is None or int(movie.get("Year")) >= start_year)
            and (end_year is None or int(movie.get("Year")) <= end_year)
        ]
        return filtered_movies

    def random_movie(self) -> Dict[str, MovieData]:
        """Return a random movie from the list.

        Returns:
            Dict[str, MovieData]: A dictionary containing movie information.
        """
        if not self.movies:
            return None
        random_movie = random.choice(list(self.movies.values()))
        return random_movie

    def search_movie(self, title: str) -> List[Dict[str, MovieData]]:
        """Search for a movie by title.

        Args:
            title (str): The title of the movie to search for.

        Returns:
            List[Dict[str, MovieData]]: A list of movies matching the search title.
        """
        title = title.lower()
        return [
            movie
            for movie in self.movies.values()
            if title in movie.get("Title", "").lower()
        ]

    def sort_by_rating(self) -> List[Dict[str, MovieData]]:
        """Sort movies by their rating in descending order.

        Returns:
            List[Dict[str, MovieData]]: A list of movies sorted by rating.
        """
        return sorted(
            self.movies.values(), key=lambda x: float(x.get("Rating", 0)), reverse=True
        )

    def sort_by_year(self) -> List[Dict[str, MovieData]]:
        """Sort movies by their release year in descending order.

        Returns:
            List[Dict[str, MovieData]]: A list of movies sorted by release year.
        """
        return sorted(
            self.movies.values(), key=lambda x: int(x.get("Year", 0)), reverse=True
        )

    def calculate_average_rating(self) -> float:
        """Calculate the average rating of the movies.

        Returns:
            float: The average rating of the movies.
        """
        if not self.movies:
            return 0.0
        total_rating = sum(
            float(movie.get("Rating", 0)) for movie in self.movies.values()
        )
        return total_rating / len(self.movies)

    def find_best_movies(self, top_n=10) -> List[Dict[str, MovieData]]:
        """Find the top N best-rated movies.

        Args:
            top_n (int): The number of top movies to find.

        Returns:
            List[Dict[str, MovieData]]: A list of the top N best-rated movies.
        """
        sorted_movies = sorted(
            self.movies.values(), key=lambda x: float(x.get("Rating", 0)), reverse=True
        )
        return sorted_movies[:top_n]

    def find_worst_movies(self, top_n=10) -> List[Dict[str, MovieData]]:
        """Find the top N worst-rated movies.

        Args:
            top_n (int): The number of worst movies to find.

        Returns:
            List[Dict[str, MovieData]]: A list of the top N worst-rated movies.
        """
        sorted_movies = sorted(
            self.movies.values(), key=lambda x: float(x.get("Rating", 0))
        )
        return sorted_movies[:top_n]

    def get_movies_statistics(self) -> Dict[str, MovieData]:
        """Compute and return statistics about the movies.

        Returns:
            Dict[str, MovieData]: A dictionary containing statistics about the movies.
        """
        num_movies = len(self.movies)
        average_rating = self.calculate_average_rating()
        best_movies = self.find_best_movies(top_n=5)
        worst_movies = self.find_worst_movies(top_n=5)

        return {
            "total_movies": num_movies,
            "average_rating": average_rating,
            "best_movies": best_movies,
            "worst_movies": worst_movies,
        }
