from django.shortcuts import render

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def movies_index(request):
    return render(request, 'movies/index.html', {'movies': movies})

class Movie:
    def __init__(self, title, genre, year, director, description, poster):
        self.title = title
        self.genre = genre
        self.year = year
        self.director = director
        self.description = description
        self.poster = poster

movies = [
    Movie('Bladerunner', 'Sci-Fi', '1982', 'Ridley Scott', 'In a cyberpunk vision of the future, man has developed the technology to create replicants - humanoid androids with short, fixed lifespans - which are illegal on Earth, but are used in the off-world colonies.', 'no image')
]