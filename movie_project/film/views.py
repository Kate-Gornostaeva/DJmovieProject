from django.shortcuts import render
from .models import Film

def index(request):
    films = Film.objects.all()
    return render(request, 'film/index.html', {'films': films})

def about(request):
    return render(request, 'film/about.html')