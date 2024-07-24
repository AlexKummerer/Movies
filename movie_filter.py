from typing import Any, Dict


def filter_movies_by_rating_and_year(
    min_rating: float, start_year: int, end_year: int, movies: Dict[str, Dict[str, Any]]
):
    """
    Filter movies based on a user-specified rating and year range.
    """

    if not movies:
        print("No movies available to filter.")
        return

    filtered_movies = [
        movie
        for movie in movies
        if movie["Rating"] >= min_rating and start_year <= movie["Year"] <= end_year
    ]

    if not filtered_movies:
        print(
            f"No movies found with a rating of {min_rating} or higher between {start_year} and {end_year}."
        )
        return

    print(
        f"\nMovies with a rating of {min_rating} or higher between {start_year} and {end_year}:"
    )
    for movie in filtered_movies:
        print(
            f"Title: {movie['Title']}, Year: {movie['Year']}, Rating: {movie['Rating']}"
        )


alist = [4, 2, 8, 6, 5]
blist = alist.copy()
blist[3] = 999
print(alist)
