from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import RegistrationForm, EnterForm, AddFilm, AddReview
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
import re
import json
import datetime
from django.views.generic import View
from myapp.models import Film, Review


class Start(View):
    def get(self, request):
        return render(request, 'start_page.html')

    def post(self, request):
        if request.method == 'POST':
            if 'sign_in' in request.POST:
                return HttpResponseRedirect('/signin/')
            elif 'sign_up' in request.POST:
                return HttpResponseRedirect('/signup/')


def sign_in(request):
    errors = []
    if request.method == 'POST':
        if 'reg' in request.POST:
            return HttpResponseRedirect('/signup/')
        form = EnterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/login/')
            else:
                errors.append('Неверно введён логин или пароль')
    else:
        form = EnterForm()
    return render(request, 'signIn.html', {'form': form, 'errors': errors})


def sign_up(request):
    errors = []
    success = ''
    if request.method == 'POST':
        if 'signIn' in request.POST:
            return HttpResponseRedirect('/signin/')
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']

            users = User.objects.all()
            usernames = []
            for x in users:
                usernames.append(x.username)

            if form.cleaned_data['password'] != form.cleaned_data['password2']:
                errors.append('Пароли должны совпадать')
            elif usernames.count(username) != 0:
                errors.append('Такой логин уже занят')
            else:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                    email=form.cleaned_data['email'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name']
                )
                user.save()
                return HttpResponseRedirect('/signin/')

    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form, 'errors': errors, 'success': success})


class FilmsList(View):
    def post(self, request):
        users = User.objects.all()
        online = False
        for user in users:
            if user.is_authenticated():
                online = True

        if request.method == 'POST':
            if 'logout' in request.POST:
                auth.logout(request)
                return HttpResponseRedirect('/signin/')

            if online:
                form = AddFilm(request.POST, request.FILES)
                if form.is_valid():
                    description = request.POST.get('description')
                    film = Film(name=form.cleaned_data['title'], description=description,
                                author=form.cleaned_data['author'], country=form.cleaned_data['country'],
                                picture=form.cleaned_data['image'])
                    film.save()
                    url = '/film_info/' + str(film.id) + '/'
                    return HttpResponseRedirect(url)
            else:
                return HttpResponseRedirect('/signin/')

    def get(self, request):
        amount_films = Film.objects.all().count()
        amount_pages = 0
        if amount_films % 3 == 1 or amount_films % 3 == 2:
            amount_pages = int(amount_films / 3 + 1)
        elif amount_films % 3 == 0:
            amount_pages = amount_films / 3

        form = AddFilm(request.POST or None)
        return render(request, 'endReg.html', {'pages': amount_pages, 'form': form,
                                               'username': auth.get_user(request).username})


class FilmInfo(View):
    def post(self, request, id_film):
        if request.method == 'POST':
            print(id_film)
            if 'back' in request.POST:
                return HttpResponseRedirect('/login/')

    def get(self, request, id_film):
        form = AddReview(request.POST or None)

        new_list = []
        reviews = Review.objects.all()

        film = Film.objects.get(id=id_film)

        for review in reviews:
            if int(id_film) == review.film_id_id:
                review_dict = dict()
                review_dict['title'] = review.title
                review_dict['review_text'] = review.review_text
                review_dict['publication_date'] = review.publication_date
                user = User.objects.get(id=review.user_id_id)
                review_dict['username'] = user.username
                review_dict['first_name'] = user.first_name
                review_dict['last_name'] = user.last_name
                new_list.append(review_dict)

        return render(request, 'film_info.html', {'form': form, 'film': film, 'reviews': new_list,
                                                  'username': auth.get_user(request).username})


@csrf_exempt
def add_review(request):
    if request.method == 'POST':
        response_data = dict()
        response_data['result'] = 'Create post successful!'

        title = request.POST.get('title')
        title_text = request.POST.get('description')
        publication_date = datetime.datetime.today().strftime("%Y-%m-%d")
        user_id = request.user.id

        url = request.POST.get('film_url')
        digit = re.sub(r'[^0-9]', '', url)
        film_id = digit

        review = Review(title=title, review_text=title_text, publication_date=publication_date,
                        user_id_id=user_id, film_id_id=film_id)
        review.save()

        response_data['title'] = title
        response_data['title_text'] = title_text
        response_data['publication_date'] = publication_date
        user = User.objects.get(id=review.user_id_id)
        response_data['username'] = user.username
        response_data['first_name'] = user.first_name
        response_data['last_name'] = user.last_name

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type='application/json'
        )


def infinite_scroll(request):
    if request.method == 'POST':
        films = Film.objects.all()

        page_number = 1
        first = 1
        if request.POST.get('page_number') != 0:
            page_number = int(request.POST.get('page_number'))
            first = (int(page_number)-1) * 3 + 1
        last = page_number * 3

        current_films = []
        number_current_film = 1

        for film in reversed(films):
            if (number_current_film >= first) and (number_current_film <= last):
                current_films.append(film)
            number_current_film += 1

        return render(request, 'films_list.html', {'films': current_films})
