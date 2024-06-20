from movie_storage import list_movies




def search_movie(title: str):
    """Search for the movie by given title"""
    movies = list_movies()
    searched_movies = [
        movie for movie in movies if title.lower() in movie["Title"].lower()
    ]
    if not searched_movies:
        print(f"No movies found containing '{title}'.")
    else:
        print(f"\nMovies matching '{title}':")
        for movie in searched_movies:
            print(
                f"Title: {movie['Title']}, Year: {movie['Year']}, Rating: {movie['Rating']}"
            )


