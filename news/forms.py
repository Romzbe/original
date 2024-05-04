from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'text', 'date']

        widgest = {
            "title": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Название статьи'}),
            "anons": TextInput(attrs={
                'class': 'from-control',
                'placeholder': 'Anons статьи',
            }),
            "date": DateTimeInput(attrs={
                'class': 'from-control',
                'placeholder': 'Data статьи'
            }),
            "text": Textarea(attrs={
                'class': 'from-control',
                'placeholder': 'Text статьи'
            })
        }