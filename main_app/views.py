from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from.models import Movie, Review
# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def movies_index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})

def movies_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movies/detail.html', { 'movie': movie })

def reviews_index(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/index.html', {'reviews': reviews})

def reviews_detail(request, review_id):
    review = Review.objects.get(id=review_id)
    return render(request, 'reviews/detail.html', {'review': review})

# Add def assoc_review???


class ReviewCreate(CreateView):
    model = Review
    fields = ['title', 'description', 'rating']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MovieCreate(CreateView):
    model = Movie
    fields = ['title', 'genre', 'year', 'director', 'description', 'poster']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReviewUpdate(UpdateView):
  model = Review
  fields = ['title', 'description', 'rating']

class ReviewDelete(DeleteView):
  model = Review
  success_url = '/reviews/'

class MovieUpdate(UpdateView):
  model = Movie
  fields = ['title', 'genre', 'year', 'director', 'description', 'poster']

class MovieDelete(DeleteView):
  model = Movie
  success_url = '/movies/'