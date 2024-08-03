import csv
import sys
import os
import logging
import argparse


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from src.app.movie_app import MovieApp
from src.storage.storage_json import JsonStorage
from src.storage.storage_csv import CsvStorage
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_empty_file(file_path: str):
    _, ext = os.path.splitext(file_path)
    if ext.lower() == ".json":
        with open(file_path, "w") as f:
            f.write("{}")  # Write an empty JSON object
    elif ext.lower() == ".csv":
        with open(file_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Title", "Year", "Rating", "Poster"])  # Write CSV headers


def get_storage(file_path: str):
    _, ext = os.path.splitext(file_path)
    if ext.lower() == ".json":
        return JsonStorage(file_path)
    elif ext.lower() == ".csv":
        return CsvStorage(file_path)
    else:
        raise ValueError(f"Unsupported file extension: {ext}")


def main() -> None:
    """
    Main function to run the movie database application.
    """
    parser = argparse.ArgumentParser(description="Movie Database Application")
    parser.add_argument("storage_file", type=str, help="The storage file (json or csv)")

    args = parser.parse_args()
    storage_file = args.storage_file

    data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
    storage_file_path = os.path.join(data_dir, storage_file)

    if not os.path.exists(storage_file_path):
        logger.error(f"File '{storage_file_path}' does not exist.")
        create_empty_file(storage_file_path)

    try:
        storage = get_storage(storage_file_path)
        app = MovieApp(storage)
        app.run()
    except Exception as e:
        logger.error(f"Failed to start the application: {e}")


if __name__ == "__main__":
    main()
