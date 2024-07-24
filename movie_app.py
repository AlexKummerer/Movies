from IStorage import IStorage
from movie_filter import filter_movies_by_rating_and_year
from movie_search import search_movie
from movie_stats import print_random_movie, sort_by_rating, sort_by_year, stats


class MovieApp:
    def __init__(self, storage: IStorage):
        self._storage = storage

    def _command_list_movies(self):
        movies = self._storage.load_movies()
        print(f"\n{len(movies)} movies in total\n")
        print(movies.items())
        for movie, details in movies.items():
            print(f"{movie} ({details['Year']}): {details['Rating']}")

    def _command_add_movie(self):
        try:
            title = input("Enter new movie name: ")
            year = int(input("Enter new movie year: "))
            rating = float(input("Enter new movie rating: "))
            poster = input("Enter new movie poster: ")
            self._storage.add_movie(title, year, rating, poster)
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

    def _command_movie_stats(self): 
        stats(self._storage.load_movies())
        
    def _command_random_movie(self):
        print_random_movie(self._storage.load_movies())
        
    def _command_search(self):
        search_title = input("Enter part of movie name: ")
        search_movie(search_title, self._storage.load_movies())
        
    def _command_sort_by_rating(self):
        sort_by_rating(self._storage.load_movies())
        
    
    def _command_sort_by_year(self):
        sort_by_year(self._storage.load_movies())
    
    def _command_filter_movie(self):
        try:
            min_rating = float(input("Enter the minimum rating to filter by: "))
            start_year = int(input("Enter the start year to filter by: "))
            end_year = int(input("Enter the end year to filter by: "))
            filter_movies_by_rating_and_year(min_rating, start_year, end_year, self._storage.load_movies())
        except ValueError:
            print("Pls enter a valid float for rating and an int for year range")
    

    def _generate_website(self): ...


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
    }

    def run(self):
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