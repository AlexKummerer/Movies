from IStorage import IStorage


class MovieApp:
    def __init__(self, storage: IStorage):
        self._storage = storage

    def _command_list_movies(self):
        self._storage.list_movies()

    def _command_add_movie(self):
        try:
            title = input("Enter new movie name: ")
            year = int(input("Enter new movie year: "))
            rating = float(input("Enter new movie rating: "))
            self._storage.add_movie(title, year, rating)
        except ValueError:
            print(
                "\nInvalid input. Year should be an integer and rating should be a float."
            )

    def _command_delete_movie(self):
        """Delete a movie from the database by title."""
        title = input("\nEnter movie name to delete: ")
        self._storage.delete_movie(title)

    def _command_update_movie(self):
        movie_name = input("\nEnter movie name: ")

        try:
            new_rating = float(input("Enter new movie rating: "))
            self._storage.update_movie(movie_name, new_rating)
        except ValueError:
            print("Invalid input. Rating should be a float.")

    def _command_movie_stats(self): ...

    def _generate_website(self): ...

    menu_options = {
        "0": ("Exit", None),
        "1": ("List movies", _command_list_movies),
        "2": ("Add movie", _command_add_movie),
        "3": ("Delete movie", _command_delete_movie),
        "4": ("Update movie", _command_update_movie),
        "5": ("Stats", stats),
        "6": ("Random movie", print_random_movie),
        "7": ("Search movie", search),
        "8": ("Movies sorted by rating", sort_by_rating),
        "9": ("Movies sorted by year", sort_by_year),
        "10": ("Filter movies", filter_movie),
    }

    def run(self):
        # Print menu
        # Get use command
        # Execute command
        pass
