from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import logging


# Create your views here.


class Test(View):
    def get(self, request):
        data = {
            'peoples': [
                {'first_name': 'Artem', 'last_name': 'Belkov', 'age': 20, 'status': 'student', 'id': 1},
                {'first_name': 'Oleg', 'last_name': 'Meluzov', 'age': 20, 'status': 'student', 'id': 2},
                {'first_name': 'Alexey', 'last_name': 'Urkevich', 'age': 20, 'status': 'student', 'id': 3},
                {'first_name': 'Slavik', 'last_name': 'Tonoyan', 'age': 71, 'status': 'teacher', 'id': 4},
                {'first_name': 'Igor', 'last_name': 'Papshev', 'age': 82, 'status': 'teacher', 'id': 5},
                {'first_name': 'Serg', 'last_name': 'Bolshakov', 'age': 70, 'status': 'teacher', 'id': 6},
                {'first_name': 'Vasiliy', 'last_name': 'Kuznetsov', 'age': 21, 'status': 'teacher', 'id': 7}
            ]
        }
        logging.info(123)
        return render(request, 'peoples.html', data)


class People(View):
    def get(self, request, id):
        data = {
            'human': {
                'id': id
            }
        }
        logging.info(data)
        return render(request, 'human_info.html', data)
