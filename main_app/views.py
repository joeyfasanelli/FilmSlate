from django.shortcuts import render

from django.http import HttpResponse

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def movie_index(request):
    return render(request, 'movies/index.html', {'movies': movies})