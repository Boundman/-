from librip.iterators import *
from librip.gens import *


def print_uniq(arr):
    for i in range(len(arr)):
        print(arr[i], end='')
        if i != len(arr)-1:
            print(end=', ')


#arr = [1, 2, 3, 1, 2, 3, 4]
#arr = gen_random(1, 6, 10)
goods = [
    {'title': 'Ковёр', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'price': 1000},
    {'title': 'Диван', 'price': 500, 'color': 'yellow'},
    {'title': 'Матрас', 'color': 'white'},
    {'color': 'purple'}
]
#arr = [i for i in field(goods, 'title')]
arr = ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D', 'a', 'a', 'a', 'a', 'b', 'B', 'B']
uni = Unique(arr, ignore_case=True)
for i in uni:
    pass
print(uni.items)
