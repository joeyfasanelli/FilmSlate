from django.db import models

class Movie:
    def __init__(self, title, genre, year, director, description, poster):
        self.title = title
        self.genre = genre
        self.year = year
        self.director = director
        self.description = description
        self.poster = poster