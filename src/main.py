import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from src.app.movie_app import MovieApp
from src.storage.storage_json import JsonStorage
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main() -> None:
    """
    Main function to run the movie database application.
    """
    try:
        storage = JsonStorage()  # Default file path is taken from Config.DATABASE_URL
        app = MovieApp(storage)
        app.run()
    except Exception as e:
        logger.error(f"Failed to start the application: {e}")


if __name__ == "__main__":
    main()
