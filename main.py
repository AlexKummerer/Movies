
from storage_json import StorageJson
import movie_storage

storage = StorageJson('movies.json')
print(storage.list_movies())
storage.add_movie('The Matrix', 1999, 8.7, 'https://www.imdb.com/title/tt0133093/')
storage.add_movie('The Matrix Reloaded', 2003, 7.2, 'https://www.imdb.com/title/tt0234215/')



# def list_movies() -> None:
#     """List all movies in the database."""
#     movies = movie_storage.list_movies()
#     print(f"\n{len(movies)} movies in total\n")
#     for movie in movies:
#         print(f"{movie['Title']} ({movie['Year']}): {movie['Rating']}")


# def add_movie() -> None:
#     """Add a new movie to the database."""
#     title = input("Enter new movie name: ")
#     try:
#         year = int(input("Enter new movie year: "))
#         rating = float(input("Enter new movie rating: "))
#         movie_storage.add_movie(title, year, rating)
#     except ValueError:
#         print(
#             "\nInvalid input. Year should be an integer and rating should be a float."
#         )


# def delete_movie() -> None:
#     """Delete a movie from the database by title."""
#     title = input("\nEnter movie name to delete: ")
#     movie_storage.delete_movie(title)


# def update_movie() -> None:
#     """Update the rating of an existing movie."""
#     movie_name = input("\nEnter movie name: ")
#     movie = movie_storage.get_movie_by_title(movie_name)

#     if movie is None:
#         print(f"Movie {movie_name} doesn't exist")
#         return
#     else:
#         try:
#             new_rating = float(input("Enter new movie rating: "))
#             movie_storage.update_movie(movie_name, new_rating)
#         except ValueError:
#             print("Invalid input. Rating should be a float.")


# def search() -> None:
#     """Search for movies by part of their title."""
#     search_title = input("Enter part of movie name: ")
#     search_movie(search_title)

# def filter_movie() -> None :
#     """Ask user-specification on rating and year range and filter"""
#     try:
#         min_rating = float(input("Enter the minimum rating to filter by: "))
#         start_year = int(input("Enter the start year to filter by: "))
#         end_year = int(input("Enter the end year to filter by: "))
#         filter_movies_by_rating_and_year(min_rating, start_year, end_year)
#     except ValueError:
#         print("Pls enter a valid float for rating and an int for year range")
    

# menu_options = {
#     "0": ("Exit", None),
#     "1": ("List movies", list_movies),
#     "2": ("Add movie", add_movie),
#     "3": ("Delete movie", delete_movie),
#     "4": ("Update movie", update_movie),
#     "5": ("Stats", stats),
#     "6": ("Random movie", print_random_movie),
#     "7": ("Search movie", search),
#     "8": ("Movies sorted by rating", sort_by_rating),
#     "9": ("Movies sorted by year", sort_by_year),
#     "10":("Filter movies", filter_movie)
# }


# def display_menu() -> None:
#     """Display the application menu"""
#     print("\n******* My Movies Database *******")
#     print("Menu:")
#     for key, (descr, _) in menu_options.items():
#         print(f"{key}. {descr}")


def main() -> None:
    pass
    # """Main function to run the application"""
    # while True:
    #     display_menu()
    #     choice = input(f"Enter choice (0-{len(menu_options) -1 }): ").strip()
    #     if choice in menu_options:
    #         descr, function = menu_options[choice]
    #         if choice == "0":
    #             print("\nExiting the application, Goodbye!")
    #             break
    #         print(f"\nExecuting: {descr}")
    #         function()
    #     else:
    #         print(
    #             f"\nInvalid choice. Please enter a number between 0 and {len(menu_options) -1 }."
    #         )

    #     input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()
