from movie_storage import list_movies


def filter_movies_by_rating_and_year(min_rating, start_year, end_year):
    """
    Filter movies based on a user-specified rating and year range.
    """
    movies = list_movies()

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
