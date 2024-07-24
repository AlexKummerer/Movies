from movie_app import MovieApp
from storage_json import StorageJson


def main() -> None:
    """
    Main function to run the movie database application.
    """
    storage = StorageJson("movies.json")
    app = MovieApp(storage)
    app.run()


if __name__ == "__main__":
    main()
