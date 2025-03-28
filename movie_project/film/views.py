from django.shortcuts import render, redirect
from .models import Film
from .forms import FilmForm

def index(request):
    error = ''
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('film:about')
        else:
            error = 'Форма была неверной'

    form = FilmForm

    return render(request, 'film/index.html', {'form': form} )

def about(request):
    films = Film.objects.all()
    return render(request, 'film/about.html', {'films': films})