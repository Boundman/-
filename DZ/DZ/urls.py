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
from myapp.views import signIn, signUp, endreg, start, addFilm, filmInfo, addReview, infiniteScroll

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/infinite_scroll', infiniteScroll, name='infinite_scroll'),
    url(r'^login/', endreg),
    url(r'^signin/', signIn),
    url(r'^signup/', signUp),
    url(r'^start/', start),
    url(r'^add_Film/', addFilm),
    url(r'^film_info/add_review', addReview),
    url(r'^film_info/(?P<id>\d+)', filmInfo, name='film_info'),
]