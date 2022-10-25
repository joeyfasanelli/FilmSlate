from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from.models import Review
import requests

#TMBD_API_KEY = "27866702f39bce28cfa7752a49f16399"


# API Search Query with TMDB API


def search(request):
  query = request.GET.get('q')

  if query:
    data = requests.get(f"https://api.themoviedb.org/3/search/{request.GET.get('type')}?api_key=27866702f39bce28cfa7752a49f16399&language=en-US&page=1&include_adult=false&query={query}")


  else:
    return HttpResponse("Please enter a search query")
  
  return render(request, "results.html", {'data': data.json(), "type": request.GET.get('type')})




# APP ROUTES

def home(request):
    return render(request, 'home.html')



def about(request):
    return render(request, 'about.html')



def view_tv_detail(request, tv_id):
  data = requests.get(f"https://api.themoviedb.org/3/tv/{tv_id}?api_key=27866702f39bce28cfa7752a49f16399&language=en-US")
  return render(request, 'tv_detail.html', {'data': data.json()})



def view_movie_detail(request, movie_id):
  data = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=27866702f39bce28cfa7752a49f16399&language=en-US")
  return render(request, 'movie_detail.html', {'data': data.json()})



def view_trending_results(request):
  type = request.GET.get('type') if request.GET.get('type') else "all"
  trendings = requests.get(f"https://api.themoviedb.org/3/trending/{type}/week?api_key=27866702f39bce28cfa7752a49f16399&language=en-US")
  return JsonResponse(trendings.json())


@login_required
def review_page(request, movie_id):
  if request.method == "POST":
    user = request.user
    review = request.POST.get("review")

    if not request.user.is_authenticated:
      user = User.objects.get(id=1)

    Review(review=review, user=user, movie_id=movie_id).save()

    return redirect(f"/movie/{movie_id}/reviews")
  
  else:
    data = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=27866702f39bce28cfa7752a49f16399&language=en-US")
    title = data.json()["title"]

    reviews = reversed(Review.objects.filter(movie_id=movie_id))

    return render(request, "reviews.html", {"title": title, "reviews": reviews})





# @login_required
# def movies_index(request):
#     movies = Movie.objects.filter(user=request.user)
#     return render(request, 'movies/index.html', {'movies': movies})

# @login_required
# def movies_detail(request, movie_id):
#     movie = Movie.objects.get(id=movie_id)
#     return render(request, 'movies/detail.html', { 'movie': movie })

# @login_required
# def reviews_index(request):
#     reviews = Review.objects.all()
#     return render(request, 'reviews/index.html', {'reviews': reviews})

# @login_required
# def reviews_detail(request, review_id):
#     review = Review.objects.get(id=review_id)
#     return render(request, 'reviews/detail.html', {'review': review})

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
      return redirect('home')
    else:
      error_message = 'Invalid sign up, please try again.'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# Add def assoc_review???




class ReviewCreate(CreateView):
    model = Review
    fields = ['review', 'rating']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# class MovieCreate(LoginRequiredMixin, CreateView):
#     model = Movie
#     fields = ['title', 'genre', 'year', 'director', 'description', 'poster']
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
    
class ReviewUpdate(LoginRequiredMixin, UpdateView):
  model = Review
  fields = ['review']

class ReviewDelete(LoginRequiredMixin, DeleteView):
  model = Review
  success_url = '/'

# class MovieUpdate(LoginRequiredMixin, UpdateView):
#   model = Movie
#   fields = ['title', 'genre', 'year', 'director', 'description', 'poster']

# class MovieDelete(LoginRequiredMixin, DeleteView):
#   model = Movie
#   success_url = '/movies/'