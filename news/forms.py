from .models import Article
from django.forms import ModelForm, TextInput, DateInput, Textarea

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title','anounce','full_text','date']
        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder':'Название статьи'}),
            "anounce": TextInput(attrs={'class': 'form-control', 'placeholder': 'Анонс статьи'}),
            "full_text": Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст статьи'}),
            "data": DateInput(attrs={'class': 'form-control', 'placeholder':'Дата публикации'})
        }