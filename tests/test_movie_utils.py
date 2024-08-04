import pytest
import src.app.movie_utils as movie_utils

@pytest.fixture
def sample_movies():
    return {
        "The Matrix": {
            "Title": "The Matrix",
            "Year": 1999,
            "Rating": 8.7,
            "Poster": "http://example.com/poster.jpg",
            "Notes": "",
            "ImdbID": "tt0133093"
        },
        "Inception": {
            "Title": "Inception",
            "Year": 2010,
            "Rating": 8.8,
            "Poster": "http://example.com/poster.jpg",
            "Notes": "",
            "ImdbID": "tt1375666"
        }
    }

def test_filter_movies_by_rating_and_year(sample_movies):
    utils = movie_utils.MovieUtils(sample_movies)
    result = utils.filter_movies_by_rating_and_year(8.7, 1990, 2000)
    assert len(result) == 1

def test_random_movie(sample_movies):
    utils = movie_utils.MovieUtils(sample_movies)
    result = utils.random_movie()
    assert result["Title"] in ["The Matrix", "Inception"]

def test_search_movie(sample_movies):
    utils = movie_utils.MovieUtils(sample_movies)
    result = utils.search_movie("Matrix")
    assert len(result) == 1
    assert result[0]["Title"] == "The Matrix"
