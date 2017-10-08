import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = 'C:\\data_light_cp1251.json'

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path) as f:
    data = json.load(f)

goods = [
    {'title': 'Ковёр', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Матрас', 'color': 'white'},
    {'price': 1000},
    {'title': 'Матрас', 'color': 'white'},
    {'title': 'Диван', 'price': 500, 'color': 'yellow'},
    {'title': 'Матрас', 'color': 'white'},
    {'title': 'Матрас', 'color': 'white'},
    {'color': 'purple'}
]
# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def f1(arg):
    uni = unique([i for i in field(arg, 'job-name')], ignore_case=True)
    for i in uni:
        pass
    return uni.items


@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith('программист') or x.startswith('Программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    salary = [x for x in gen_random(100000, 200000, len(arg))]
    arg = [x+', зарплата {} руб'.format(y) for x, y in zip(arg, salary)]
    return arg


with timer():
    f4(f3(f2(f1(data))))
