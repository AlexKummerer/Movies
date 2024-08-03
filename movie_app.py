from IStorage import IStorage
from movie_utils import MovieUtils


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
        print(f"\n{len(movies)} movies in total\n")
        for movie, details in movies.items():
            print(f"{movie} ({details['Year']}): {details['Rating']}")

    def _command_add_movie(self) -> None:
        """
        Add a new movie to the database.
        """
        try:
            title = input("Enter new movie name: ")
            movie = self._storage.load_movies_api(title)
            print(movie)
            if movie:
                self._storage.add_movie(
                    movie["Title"], movie["Year"], movie["imdbRating"], movie["Poster"]
                )
            else:
                print(f"Movie '{title}' not found.")
        except KeyError as e:
            print(f"Error adding movie: {e}")

    def _command_delete_movie(self) -> None:
        """Delete a movie from the database by title."""
        title = input("\nEnter movie name to delete: ")
        self._storage.delete_movie(title)

    def _command_update_movie(self) -> None:
        """
        Update the rating of a movie in the database.
        """
        movie_name = input("\nEnter movie name: ")

        try:
            new_rating = float(input("Enter new movie rating: "))
            self._storage.update_movie(movie_name, new_rating)
        except ValueError:
            print("Invalid input. Rating should be a float.")

    def _command_movie_stats(self) -> None:
        """
        Display statistics for the movie database.
        """
        statistics = self.utils.get_movies_statistics()
        print(
            f"\nStatistics for {len(self._storage. v())} movies in the database:"
        )
        print(f"Average rating: {statistics['average_rating']:.2f}")
        print("\nBest movie(s) by rating:")
        for movie in statistics["best_movies"]:
            print(f"{movie['Title']} ({movie['Year']}): {movie['Rating']}")
        print("\nWorst movie(s) by rating:")
        for movie in statistics["worst_movies"]:
            print(f"{movie['Title']} ({movie['Year']}): {movie['Rating']}")
        print("\n")

    def _command_random_movie(self) -> None:
        """
        Print a random movie and its rating from the database.
        """
        random_movie = self.utils.random_movie()
        if random_movie:
            print(
                f"\nRandom movie: {random_movie['Title']} ({random_movie['Year']}): {random_movie['Rating']}"
            )

    def _command_search(self) -> None:
        """
        Search for a movie by title.
        """
        search_title = input("Enter part of movie name: ")
        movie = self.utils.search_movie(search_title)
        if not movie:
            print(f"No movies found containing '{search_title}'.")
        else:
            print(f"\nMovies matching '{search_title}':")
            for movie in movie:
                print(
                    f"Title: {movie['Title']}, Year: {movie['Year']}, Rating: {movie['Rating']}"
                )
            print("\n")

    def _command_sort_by_rating(self) -> None:
        """
        Sort movies by their rating in descending order and print the sorted list.
        """
        sorted_movies = self.utils.sort_by_rating()
        print("\nMovies sorted by rating:")
        for movie in sorted_movies:
            print(f"{movie['Title']} ({movie['Year']}): {movie['Rating']}")
        print("\n")

    def _command_sort_by_year(self) -> None:
        """
        Sort movies by their release year in descending order and print the sorted list.
        """
        sorted_movies = self.utils.sort_by_year()
        print("\nMovies sorted by year:")
        for movie in sorted_movies:
            print(f"{movie['Title']} ({movie['Year']}): {movie['Rating']}")
        print("\n")

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
                print(
                    f"No movies found with a rating of {min_rating} or higher between {start_year} and {end_year}."
                )
                return
            print(
                f"\nMovies with a rating of {min_rating} or higher between {start_year} and {end_year}:"
            )
            for movie in filtered_movies:
                print(f"{movie['Title']} ({movie['Year']}): {movie['Rating']}")
            print("\n")
        except ValueError:
            print("Pls enter a valid float for rating and an int for year range")

    def _command_generate_website(self):
        self._storage.generate_website()
        
        
    def display_menu(self) -> None:
        """Display the application menu"""
        print("\n******* My Movies Database *******")
        print("Menu:")
        for key, (descr, _) in self.menu_options.items():
            print(f"{key}. {descr}")
            

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
        Run the movie database application
        """
        while True:
            self.display_menu()
            choice = input(f"Enter choice (0-{len(self.menu_options) -1 }): ").strip()
            if choice in self.menu_options:
                descr, function = self.menu_options[choice]
                if choice == "0":
                    print("\nExiting the application, Goodbye!")
                    break
                print(f"\nExecuting: {descr}")
                function(self)
            else:
                print(
                    f"\nInvalid choice. Please enter a number between 0 and {len(self.menu_options) -1 }."
                )

            input("\nPress Enter to return to the menu...")
