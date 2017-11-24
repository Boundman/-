from django.shortcuts import render, HttpResponse
from django.views import View
from myapp.models import Film, User, Review
# Create your views here.


class Test(View):
    def get(self, request):
        films = Film.objects.all()
        data = {
            'films': films
        }
        return render(request, 'info_file.html', data)
