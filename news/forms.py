from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from django.core.exceptions import ValidationError


class ArticlesForms(ModelForm):
    class Meta:
        model=Articles
        fields=['title', 'anons', 'full_text', 'date', 'avtor', 'status', 'room']

        widgets={
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статей'}),

            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'}),

            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'}),

            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст'}),

            "room": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Комната чата'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if title == '12345':
            raise ValidationError('Название не должно быть 12345')
        return title
