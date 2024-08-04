"""
MovieApp class to manage the movie database application.

Returns:
    _type_: None
"""

import logging
from src.storage.i_storage import IStorage
from src.app.movie_utils import MovieUtils

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MovieApp:
    """
    MovieApp class to manage the movie database application.
    """

    def __init__(self, storage: IStorage) -> None:
        """
        Initialize the MovieApp with a storage object.

        Args:
            storage (IStorage): The storage object to use for the movie database.
        """
        self._storage = storage
        self.utils = MovieUtils(self._storage.load_movies_file())

    def _command_list_movies(self) -> None:
        """
        List all movies in the database.
        """
        movies = self._storage.load_movies_file()
        logger.info("\n%d movies in total\n", len(movies))
        for movie, details in movies.items():
            logger.info("%s (%d): %f", movie, details["Year"], details["Rating"])

    def _command_add_movie(self) -> None:
        """
        Add a new movie to the database.
        """
        try:
            title = input("Enter new movie name: ")
            movie = self._storage.load_movies_api(title)
            if movie:
                self._storage.add_movie(
                    movie={
                        "Title": movie["Title"],
                        "Year": movie["Year"],
                        "Rating": movie["Rating"],
                        "Poster": movie["Poster"],
                        "Notes": "",
                        "ImdbID": movie["ImdbID"],
                    }
                )
            else:
                logger.info("Movie '%s' not found.", title)
        except KeyError as e:
            logger.error("Error adding movie: %s", e)

    def _command_delete_movie(self) -> None:
        """
        Delete a movie from the database by title.
        """
        title = input("\nEnter movie name to delete: ")
        try:
            self._storage.delete_movie(title)
            logger.info("Movie '%s' deleted.", title)
        except KeyError as e:
            logger.error("Error deleting movie: %s", e)

    def _command_update_movie(self) -> None:
        movie_name = input("\nEnter movie name: ")
        try:
            notes = input("Enter movie notes: ")
            self._storage.update_movie(movie_name, notes)
            logger.info("Movie '%s' successfully updated.", movie_name)
        except KeyError as e:
            logger.error("Error updating movie: %s", e)

    def _command_movie_stats(self) -> None:
        """
        Display statistics for the movie database.
        """
        statistics = self.utils.get_movies_statistics()
        logger.info(
            "\nStatistics for %d movies in the database:", statistics["total_movies"]
        )
        logger.info("Average rating: %.2f", statistics["average_rating"])
        logger.info("\nBest movie(s) by rating:")
        for movie in statistics["best_movies"]:
            logger.info("%s (%d): %f", movie["Title"], movie["Year"], movie["Rating"])
        logger.info("\nWorst movie(s) by rating:")
        for movie in statistics["worst_movies"]:
            logger.info("%s (%d): %f", movie["Title"], movie["Year"], movie["Rating"])

        logger.info("\n")

    def _command_random_movie(self) -> None:
        """
        Print a random movie and its rating from the database.
        """
        random_movie = self.utils.random_movie()
        if random_movie:
            logger.info(
                "\nRandom movie: %s (%d): %f",
                random_movie["Title"],
                random_movie["Year"],
                random_movie["Rating"],
            )

    def _command_search(self) -> None:
        """
        Search for a movie by title.
        """
        search_title = input("Enter part of movie name: ")
        movies = self.utils.search_movie(search_title)
        if not movies:
            logger.info("No movies found containing '%s'.", search_title)
        else:
            logger.info("\nMovies matching '%s':", search_title)
            for movie in movies:
                logger.info(
                    "Title: %s, Year: %d, Rating: %f",
                    movie["Title"],
                    movie["Year"],
                    movie["Rating"],
                )
            logger.info("\n")

    def _command_sort_by_rating(self) -> None:
        """
        Sort movies by their rating in descending order and print the sorted list.
        """
        sorted_movies = self.utils.sort_by_rating()
        logger.info("\nMovies sorted by rating:")
        for movie in sorted_movies:
            logger.info("%s (%d): %f", movie["Title"], movie["Year"], movie["Rating"])
        logger.info("\n")

    def _command_sort_by_year(self) -> None:
        """
        Sort movies by their release year in descending order and print the sorted list.
        """
        sorted_movies = self.utils.sort_by_year()
        logger.info("\nMovies sorted by year:")
        for movie in sorted_movies:
            logger.info("%s (%d): %f", movie["Title"], movie["Year"], movie["Rating"])
        logger.info("\n")

    def _command_filter_movie(self) -> None:
        """
        Filter movies by minimum rating and release year range.
        """
        try:
            min_rating = float(input("Enter the minimum rating to filter by: "))
            start_year = int(input("Enter the start year to filter by: "))
            end_year = int(input("Enter the end year to filter by: "))

            filtered_movies = self.utils.filter_movies_by_rating_and_year(
                min_rating, start_year, end_year
            )
            if not filtered_movies:
                logger.info(
                    "No movies found with a rating of %f or higher between %d and %d.",
                    min_rating,
                    start_year,
                    end_year,
                )
                return
            logger.info(
                "\nMovies with a rating of %f or higher between %d and %d:",
                min_rating,
                start_year,
                end_year,
            )
            for movie in filtered_movies:
                logger.info(
                    "%s (%d): %f", movie["Title"], movie["Year"], movie["Rating"]
                )
            logger.info("\n")
        except ValueError:
            logger.error(
                "Please enter a valid float for rating and an int for year range"
            )

    def _command_generate_website(self) -> None:
        """
        Generate the movie website.
        """
        self._storage.generate_website()

    def display_menu(self) -> None:
        """Display the application menu."""
        logger.info("\n******* My Movies Database *******")
        logger.info("Menu:")
        for key, (descr, _) in self.menu_options.items():
            logger.info("%s. %s", key, descr)

    menu_options = {
        "0": ("Exit", None),
        "1": ("List movies", _command_list_movies),
        "2": ("Add movie", _command_add_movie),
        "3": ("Delete movie", _command_delete_movie),
        "4": ("Update movie", _command_update_movie),
        "5": ("Stats", _command_movie_stats),
        "6": ("Random movie", _command_random_movie),
        "7": ("Search movie", _command_search),
        "8": ("Movies sorted by rating", _command_sort_by_rating),
        "9": ("Movies sorted by year", _command_sort_by_year),
        "10": ("Filter movies", _command_filter_movie),
        "11": ("Generate website", _command_generate_website),
    }

    def run(self) -> None:
        """
        Run the movie database application.
        """
        while True:
            self.display_menu()
            choice = input(f"Enter choice (0-{len(self.menu_options) - 1}): ").strip()
            if choice in self.menu_options:
                descr, function = self.menu_options[choice]
                if choice == "0":
                    logger.info("\nExiting the application. Goodbye!")
                    break
                logger.info("\nExecuting: %s", descr)
                function(self)
            else:
                logger.warning(
                    "\nInvalid choice. Please enter a number between 0 and %d.",
                    len(self.menu_options) - 1,
                )

            input("\nPress Enter to return to the menu...")
