import movie_storage
from movie_stats import stats
from movie_search import print_random_movie, search_movie, sort_by_rating


def list_movies():
    movies = movie_storage.list_movies()
    print(f"\n{len(movies)} movies in total\n")
    for movie in movies:
        print(f"{movie['Title']} ({movie['Year']}): {movie['Rating']}")


def add_movie():

    title = input("Enter new movie name: ")
    try:
        year = int(input("Enter new movie year: "))
        rating = float(input("Enter new movie rating: "))
    except ValueError:
        print(
            "\nInvalid input. Year should be an integer and rating should be a float."
        )

    movie_storage.add_movie(title, year, rating)


def delete_movie():
    title = input("\nEnter movie name to delete: ")
    movie_storage.delete_movie(title)


def update_movie():
    movie_name = input("\nEnter movie name: ")
    movie = movie_storage.get_movie_by_title(movie_name)

    if movie is None:
        print(f"Movie {movie_name} doesn't exist")
    else:
        try:
            new_rating = float(input("Enter new movie rating: "))
            movie_storage.update_movie(movie_name, new_rating)
        except ValueError:
            print("Invalid input. Rating should be a float.")


def search():
    search_title = input("Enter part of movie name: ")
    search_movie(search_title)


menu_options = {
    "0": ("Exit", None),
    "1": ("List movies", list_movies),
    "2": ("Add movie", add_movie),
    "3": ("Delete movie", delete_movie),
    "4": ("Update movie", update_movie),
    "5": ("Stats", stats),
    "6": ("Random movie", print_random_movie),
    "7": ("Search movie", search),
    "8": ("Movies sorted by rating", sort_by_rating),
}


def display_menu():
    """Display the application menu"""
    print("\n******* My Movies Database *******")
    print("Menu:")
    for key, (descr, _) in menu_options.items():
        print(f"{key}. {descr}")


def main():
    """Main function to run the application"""
    while True:
        display_menu()
        choice = input(f"Enter choice (0-{len(menu_options) -1 }): ").strip()
        if choice in menu_options:
            descr, function = menu_options[choice]
            if choice == "0":
                print("\nExiting the application, Goodbye!")
                break
            else:
                print(f"\nExecuting: {descr}")
                function()
        else:
            print(
                f"\nInvalid choice. Please enter a number between 0 and {len(menu_options) -1 }."
            )

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()
