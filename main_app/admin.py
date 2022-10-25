from django.contrib import admin
from .models import MovieReview, TvReview

admin.site.register(MovieReview)
admin.site.register(TvReview)