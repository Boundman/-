from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import RegistrationForm, EnterForm
from django.contrib.auth.models import User
from django.contrib import auth
import django.contrib.admin
#from myapp.models import User


# Create your views here.


def start(request):
    if request.method == 'POST':
        if 'sign_in' in request.POST:
            return HttpResponseRedirect('/signin/')
        elif 'sign_up' in request.POST:
            return HttpResponseRedirect('/signup/')
    return render(request, 'start_page.html')


def signIn(request):
    errors = []
    if request.method == 'POST':
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


def signUp(request):
    errors = []
    success = ''
    if request.method == 'POST':
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
                success += 'You was successfully registered.'
                #return HttpResponseRedirect('/login/')

    else:
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form, 'errors': errors, 'success': success})


def endreg(request):
    data = {}
    if request.method == 'POST':
        user = auth.get_user(request)
        data['user'] = user
        if 'logout' in request.POST:
            auth.logout(request)
            return HttpResponseRedirect('/signin/')
    return render(request, 'endReg.html', data)
