from django import forms
from .models import *


class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=5, label='Логин')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Повторите пароль')
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')


class EnterForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')


class AddFilm(forms.Form):
    class Meta:
        model = Film
        exclude = ['title', 'description', 'author', 'country']

    title = forms.CharField(label='Название', min_length=1, max_length=100)
    description = forms.CharField(label='Описание', min_length=1, max_length=500)
    author = forms.CharField(label='Автор', min_length=5, max_length=35)
    country = forms.CharField(label='Страна', min_length=2, max_length=30)
    image = forms.FileField(label='Загрузить', allow_empty_file=True)


class AddReview(forms.Form):
    title = forms.CharField(label='Заголовок', min_length=1, max_length=50)
    reviewText = forms.CharField(label='Отзыв', min_length=1, max_length=1000)
