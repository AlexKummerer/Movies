import random
from movie_storage import list_movies

def print_random_movie():
    """Print a random movie and its rating from the database."""
    movies = list_movies()
    
    if not movies:
        print("No movies available in the database.")
        return
    
    random_movie = random.choice(movies)
    print("\nRandom Movie:")
    print(f"Title: {random_movie['Title']}")
    print(f"Rating: {random_movie['Rating']}")

def search_movie(title: str):
    """Search for the movie by given title"""
    
    movies = list_movies()

    searched_movies = [movie for movie in movies if  title.lower() in  movie["Title"].lower()  ] 
    print(searched_movies)
    for movie in searched_movies:        
        print(f'{movie["Title"]}, {movie["Rating"]} ')   


def sort_by_rating():
    movies = list_movies()   
    if not movies:
        print("No movies available to sort.")
        return
    sorted_movies = sorted(movies, key=lambda movie: movie['Rating'], reverse=True)
    print("\nMovies sorted by rating (highest to lowest):")
    for movie in sorted_movies:
        print(f"Title: {movie['Title']}, Year: {movie['Year']}, Rating: {movie['Rating']}")
    