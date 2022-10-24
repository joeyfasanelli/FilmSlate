from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from.models import Movie, Review
# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def movies_index(request):
    movies = Movie.objects.filter(user=request.user)
    return render(request, 'movies/index.html', {'movies': movies})

@login_required
def movies_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'movies/detail.html', { 'movie': movie })

@login_required
def reviews_index(request):
    reviews = Review.objects.all()
    return render(request, 'reviews/index.html', {'reviews': reviews})

@login_required
def reviews_detail(request, review_id):
    review = Review.objects.get(id=review_id)
    return render(request, 'reviews/detail.html', {'review': review})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up, please try again.'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# Add def assoc_review???


class ReviewCreate(CreateView):
    model = Review
    fields = ['title', 'description', 'rating']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MovieCreate(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['title', 'genre', 'year', 'director', 'description', 'poster']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ReviewUpdate(LoginRequiredMixin, UpdateView):
  model = Review
  fields = ['title', 'description', 'rating']

class ReviewDelete(LoginRequiredMixin, DeleteView):
  model = Review
  success_url = '/reviews/'

class MovieUpdate(LoginRequiredMixin, UpdateView):
  model = Movie
  fields = ['title', 'genre', 'year', 'director', 'description', 'poster']

class MovieDelete(LoginRequiredMixin, DeleteView):
  model = Movie
  success_url = '/movies/'