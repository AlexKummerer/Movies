"""
Description: main function to run the movie database application.

Raises:
    ValueError: If the file extension is not supported.

Returns:
    _type_: None

"""

import csv
import sys
import os
import argparse


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app.movie_app import MovieApp
from src.storage.storage_json import JsonStorage
from src.storage.storage_csv import CsvStorage


def create_empty_file(file_path: str):
    """
    Create an empty file with the given file path.

    Args:
        file_path (str):  The path to the file to create.
    """
    _, ext = os.path.splitext(file_path)
    if ext.lower() == ".json":
        with open(file_path, "w", encoding="utf-8") as f:
            f.write("{}")  # Write an empty JSON object
    elif ext.lower() == ".csv":
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Title", "Year", "Rating", "Poster", "Notes", "ImdbID"])


def get_storage(file_path: str):
    """
    Get the storage object based on the file extension.

    Args:
        file_path (str): The path to the storage file.

    Raises:
        ValueError: If the file extension is not supported.

    Returns:
        _type_:  The storage object.
    """
    _, ext = os.path.splitext(file_path)
    if ext.lower() == ".json":
        return JsonStorage(file_path)
    if ext.lower() == ".csv":
        return CsvStorage(file_path)
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
        print(f"File '{storage_file_path}' does not exist. Creating a new one...")
        create_empty_file(storage_file_path)

    try:
        storage = get_storage(storage_file_path)
        app = MovieApp(storage)
        app.run()
    except (ValueError, OSError) as e:
        print(f"Failed to start the application: {e}")


if __name__ == "__main__":
    main()
