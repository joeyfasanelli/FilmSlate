from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Review(models.Model):
    review = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review
        
    def get_absolute_url(self):
        return reverse('reviews_detail', kwargs={'review_id': self.id})