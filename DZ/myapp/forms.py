from django import forms
from .models import *


class RegistrationForm(forms.Form):
    username = forms.CharField(min_length=5, label='Логин')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Повторите пароль')
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'type': 'email', 'class': 'form-control',
                                                     'id': 'exampleInputEmail1', 'aria-describedby': 'emailHelp',
                                                     'placeholder': 'Введите Логин'})

        self.fields['password'].widget.attrs.update({'type': 'password', 'class': 'form-control',
                                                     'id': 'exampleInputPassword1', 'placeholder': 'Пароль'})

        self.fields['password2'].widget.attrs.update({'type': 'password', 'class': 'form-control',
                                                     'id': 'exampleInputPassword1', 'placeholder': 'Повторите пароль'})

        self.fields['email'].widget.attrs.update({'type': 'email', 'class': 'form-control',
                                                     'id': 'exampleInputEmail1', 'aria-describedby': 'emailHelp',
                                                     'placeholder': 'Введите Email'})

        self.fields['first_name'].widget.attrs.update({'type': 'email', 'class': 'form-control',
                                                     'id': 'exampleInputEmail1', 'aria-describedby': 'emailHelp',
                                                     'placeholder': 'Введите Имя'})

        self.fields['last_name'].widget.attrs.update({'type': 'email', 'class': 'form-control',
                                                     'id': 'exampleInputEmail1', 'aria-describedby': 'emailHelp',
                                                     'placeholder': 'Введите Фамилию'})


class EnterForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

    def __init__(self, *args, **kwargs):
        super(EnterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'type': 'email', 'class': 'form-control',
                                                     'id': 'exampleInputEmail1', 'aria-describedby': 'emailHelp',
                                                     'placeholder': 'Введите Логин'})

        self.fields['password'].widget.attrs.update({'type': 'password', 'class': 'form-control',
                                                     'id': 'exampleInputPassword1', 'placeholder': 'Пароль'})


class AddFilm(forms.Form):
    class Meta:
        model = Film
        exclude = ['title', 'description', 'author', 'country']

    title = forms.CharField(label='Название', min_length=1, max_length=100)
    author = forms.CharField(label='Автор', min_length=5, max_length=35)
    country = forms.CharField(label='Страна', min_length=2, max_length=30)
    image = forms.FileField(label='Загрузить', allow_empty_file=True)

    def __init__(self, *args, **kwargs):
        super(AddFilm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'type': 'email', 'class': 'form-control',
                                                     'id': 'exampleInputEmail1', 'aria-describedby': 'emailHelp',
                                                     'placeholder': 'Введите Название'})

        self.fields['author'].widget.attrs.update({'type': 'email', 'class': 'form-control',
                                                        'id': 'exampleInputEmail1', 'aria-describedby': 'emailHelp',
                                                        'placeholder': 'Автор'})

        self.fields['country'].widget.attrs.update({'type': 'email', 'class': 'form-control',
                                                        'id': 'exampleInputEmail1', 'aria-describedby': 'emailHelp',
                                                        'placeholder': 'Страна'})

        self.fields['image'].widget.attrs.update({'label': 'Загрузить', 'type': 'file', 'class': 'form-control-file',
                                                    'id': 'exampleFormControlFile1'})


class AddReview(forms.Form):
    title = forms.CharField(label='Заголовок', min_length=1, max_length=50)
    reviewText = forms.CharField(label='Отзыв', min_length=1, max_length=1000)

    def __init__(self, *args, **kwargs):
        super(AddReview, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'type': 'email', 'class': 'form-control',
                                                     'id': 'title', 'aria-describedby': 'emailHelp',
                                                     'placeholder': 'Введите Заголовок'})

        self.fields['reviewText'].widget.attrs.update({'type': 'email', 'class': 'form-control',
                                                  'id': 'description', 'aria-describedby': 'emailHelp',
                                                  'placeholder': 'Введите Отзыв'})
