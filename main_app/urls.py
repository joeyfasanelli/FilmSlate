from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('movies/', views.movies_index, name='index'),
    path('movies/<int:movie_id>/', views.movies_detail, name='detail'),
    path('reviews/', views.reviews_index, name='reviews_index'),
    path('reviews/<int:review_id>/', views.reviews_detail, name='reviews_detail'),
    path('reviews/create/', views.ReviewCreate.as_view(), name='reviews_create')
]