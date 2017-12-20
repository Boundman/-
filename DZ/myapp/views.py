from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import RegistrationForm, EnterForm, AddFilm, AddReview
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import re
import json
import datetime
from DZ.settings import BASE_DIR, LOGIN_URL, STATICFILES_DIRS
from myapp.models import Film, Review
import django.contrib.admin


def start(request):
    if request.method == 'POST':
        if 'sign_in' in request.POST:
            return HttpResponseRedirect('/signin/')
        elif 'sign_up' in request.POST:
            return HttpResponseRedirect('/signup/')
    return render(request, 'start_page.html')


def signIn(request):
    errors = []
    users = User.objects.all()
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
    return render(request, 'signIn.html', {'form': form, 'errors': errors, 'users': users})


def signUp(request):
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
                success += 'Вы были успешно зарегистрированы!'
                return HttpResponseRedirect('/login/')

    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form, 'errors': errors, 'success': success})


def endreg(request):
    films = Film.objects.all()
    if request.method == 'POST':
        if 'logout' in request.POST:
            auth.logout(request)
            return HttpResponseRedirect('/signin/')
        if 'addFilm' in request.POST:
            return HttpResponseRedirect('/add_Film/')
    return render(request, 'endReg.html', {'films': films})


def addFilm(request):
    if request.method == 'POST':
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
        form = AddFilm()
    return render(request, 'add_Film.html', {'form': form})


def filmInfo(request, id):
    new_list = []
    reviews = Review.objects.all()

    for review in reviews:
        if int(id) == review.film_id_id:
            review_dict = dict()
            review_dict['title'] = review.title
            review_dict['review_text'] = review.review_text
            review_dict['publication_date'] = review.publication_date
            user = User.objects.get(id=review.user_id_id)
            review_dict['username'] = user.username
            review_dict['first_name'] = user.first_name
            review_dict['last_name'] = user.last_name
            new_list.append(review_dict)

    film = Film.objects.get(id=id)

    if request.method == 'POST':
        if 'back' in request.POST:
            return HttpResponseRedirect('/login/')
        form = AddReview(request.POST)
        # if form.is_valid():
        # data = form.cleaned_data
        # title = data.get('title', '')
        # title_text = data.get('reviewText', '')
        # publication_date = datetime.datetime.now()
        # user_id = request.user.id
        # film_id = id

        # review = Review(title=title, review_text=title_text, publication_date=publication_date,
        #                user_id_id=user_id, film_id_id=film_id)
        # review.save()

        # url = '/film_info/' + str(id) + '/'
        # return HttpResponseRedirect(url)
    else:
        form = AddReview()
    return render(request, 'film_info.html', {'form': form, 'film': film, 'reviews': new_list})


@csrf_exempt
def addReview(request):
    if request.method == 'POST':
        response_data = {}
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


def infiniteScroll(request):
    if request.method == 'POST':
        response_data = {}
        response_data['result'] = 'It`s working'
        response_data['fuck'] = request.POST.get('message')
        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type='application/json'
        )
