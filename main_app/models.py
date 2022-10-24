from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    director = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    poster = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'movie_id': self.id})


class Review(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    rating = models.IntegerField(choices=list(zip(range(1, 11), range(1, 11))))
        
    def get_absolute_url(self):
        return reverse('reviews_detail', kwargs={'review_id': self.id})