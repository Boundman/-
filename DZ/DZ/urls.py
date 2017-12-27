"""DZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from myapp.views import sign_in, sign_up, FilmsList, Start, FilmInfo, add_review, infinite_scroll

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/infinite_scroll', infinite_scroll, name='infinite_scroll'),
    url(r'^login/', FilmsList.as_view(), name='films_list'),
    url(r'^signin/', sign_in),
    url(r'^signup/', sign_up),
    url(r'^start/', Start.as_view()),
    url(r'^film_info/add_review', add_review),
    url(r'^film_info/(?P<id_film>\d+)', FilmInfo.as_view(), name='film_info'),
]
