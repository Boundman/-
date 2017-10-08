from librip.gens import *


def print_list(list):
    for x in range(len(list)):
        print(list[x], end='')
        if x != len(list)-1:
            print(end=', ')


ran_digits = [x for x in gen_random(1, 5, 7)]
#ran_digits = gen_random(1, 5, 7)
print_list(ran_digits)
print()

goods = [
    {'title': 'Ковёр', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'price': 1000},
    {'title': 'Диван', 'price': 500, 'color': 'yellow'},
    {'title': 'Матрас', 'color': 'white'},
    {'color': 'purple'}
]

new_items = []
for x in field(goods, 'color', 'title'):
    new_items.append(x)
print_list(new_items)
