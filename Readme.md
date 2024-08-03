# Movie Database Application

A Python-based application to manage a movie database, with functionalities to add, delete, update, search, and list movies. It also includes features to filter movies by rating and year, sort movies, display statistics, and generate a static website to display the movies.

## Table of Contents

- Features
- Project Structure
- Installation
- Configuration
- Usage
- Contributing
- License

## Features

- Add new movies to the database
- Delete movies from the database
- Update movie ratings
- List all movies
- Search for movies by title
- Filter movies by rating and release year
- Sort movies by rating and release year
- Display statistics (total movies, average rating, best and worst movies)
- Generate a static website to display the movies

## Project Structure

movie_app/
│
├── data/
│   └── movies.json
│
├── templates/
│   ├── movie_app.html
│   └── movies_template.html
│
├── static/
│   └── style.css
│
├── src/
│   ├── storage/
│   │   ├── __init__.py
│   │   ├── IStorage.py
│   │   └── storage_json.py
│   ├── app/
│   │   ├── __init__.py
│   │   ├── movie_app.py
│   │   └── movie_utils.py
│   ├── config.py
│   └── main.py
│
├── .env
├── requirements.txt
└── README.md
## Installation

### Prerequisites
- Python 3.9+
- pip (Python package installer)

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/movie_app.git
    cd movie_app
    ```

2. Create a virtual environment:
    ```sh
    python3 -m venv .venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        .venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source .venv/bin/activate
        ```

4. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

5. Set up the environment variables:
    Create a `.env` file in the root directory of your project and add the following:
    ```env
    DATABASE_URL=./data/movies.json
    SECRET_KEY=your_secret_key
    DEBUG=True
    ```

## Configuration
Configuration settings are managed via the `.env` file and loaded using the `python-dotenv` library.

- `DATABASE_URL`: Path to the JSON file storing movie data.
- `SECRET_KEY`: Your OMDB API key.
- `DEBUG`: Enable or disable debug mode (True/False).

## Usage

1. Run the application:
    ```sh
    python src/main.py
    ```

2. Interact with the menu to manage the movie database:
    ```
    ******* My Movies Database *******
    Menu:
    0. Exit
    1. List movies
    2. Add movie
    3. Delete movie
    4. Update movie
    5. Stats
    6. Random movie
    7. Search movie
    8. Movies sorted by rating
    9. Movies sorted by year
    10. Filter movies
    11. Generate website
    Enter choice (0-11):
    ```

3. Generate the website:
    Choose option 11 from the menu to generate the static website. The generated HTML file will be located in the `templates` directory.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

## Licence
This project is licensed under the MIT License. See the LICENSE file for details.

### Explanation

- **Features**: Lists the functionalities of your application.
- **Project Structure**: Provides a visual representation of your project's directory layout.
- **Installation**: Detailed steps to set up the project locally, including cloning the repo, creating a virtual environment, and installing dependencies.
- **Configuration**: Instructions on setting up environment variables.
- **Usage**: How to run the application and interact with it.
- **Contributing**: Guidelines for contributing to the project.
- **License**: Information about the project's license.



