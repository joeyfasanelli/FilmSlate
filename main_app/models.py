from django.db import models
from django.urls import reverse

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    director = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    poster = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'movie_id': self.id})


class Review(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    rating = models.IntegerField()

    def get_absolute_url(self):
        return reverse('reviews_detail', kwargs={'pk': self.id})