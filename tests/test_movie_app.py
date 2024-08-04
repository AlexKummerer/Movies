import pytest
from unittest.mock import MagicMock, patch
from src.app.movie_details import MovieDetails
import src.storage.storage_csv as CsvStorage
import src.app.movie_app as movie_app


@pytest.fixture
def mock_storage():
    storage = MagicMock(spec=CsvStorage.CsvStorage)
    storage.load_movies_file.return_value = {}
    storage.load_movies_api.return_value = {
        "Title": "The Matrix",
        "Year": "1999",
        "imdbRating": "8.7",
        "Poster": "http://example.com/poster.jpg",
        "ImdbID": "tt0133093",
    }
    return storage


@pytest.fixture
def app(mock_storage):
    return movie_app.MovieApp(mock_storage)


def test_list_movies(app, mock_storage):
    app._command_list_movies()
    assert mock_storage.load_movies_file.call_count == 2


def test_add_movie(app, mock_storage):
    with patch("builtins.input", side_effect=["The Matrix"]):
        app._command_add_movie()
    expected_movie = MovieDetails(
        title="The Matrix",
        year=1999,
        rating=8.7,
        poster="http://example.com/poster.jpg",
        imdb_id="tt0133093",
    )
    mock_storage.add_movie.assert_called_once_with(expected_movie)

def test_delete_movie(app, mock_storage):
    with patch("builtins.input", side_effect=["The Matrix"]):
        app._command_delete_movie()
    mock_storage.delete_movie.assert_called_once()


def test_update_movie(app, mock_storage):
    with patch("builtins.input", side_effect=["The Matrix", "Great movie!"]):
        app._command_update_movie()
    mock_storage.update_movie.assert_called_once_with("The Matrix", "Great movie!")


def test_movie_stats(app):
    app._command_movie_stats()
