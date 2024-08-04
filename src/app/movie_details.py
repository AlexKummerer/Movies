""" This module contains the MovieDetails class. """

from dataclasses import dataclass


@dataclass
class MovieDetails:
    """A class to represent movie details."""

    title: str
    year: int
    rating: float
    poster: str
    imdb_id: str = ""
    notes: str = ""
