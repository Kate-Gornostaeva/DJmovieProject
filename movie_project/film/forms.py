from .models import Film
from django.forms import ModelForm, TextInput, Textarea

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['name', 'description', 'review']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Краткое содержание'}),
            'review': Textarea(attrs={'class': 'form-control', 'placeholder': 'Отзыв о фильме'}),
        }