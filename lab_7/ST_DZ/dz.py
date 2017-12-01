# Информационный вектор - 1101
# Код - Ц[7, 4]
# Способность кода - CK
# полином x**3 + x + 1
import pandas as pd


dict_err = {  # таблица ошибок по вектору синдромов № -> разряд
    '001': 0,
    '010': 1,
    '100': 2,
    '011': 3,
    '110': 4,
    '111': 5,
    '101': 6
}


def calc_err(var_in, flag):
    # 0 - вычисл. кода остатка входного вектора
    # 1 - вычисл. кода ошибки
    list_in = [int(x) for x in var_in]
    list_check = [1, 0, 1, 1]  # порождающий код

    if not flag:
        list_in_del = list_in + [0, 0, 0]

    if flag:
        list_in_del = list_in

    y = x = 0

    while y < 4:
        if not list_in_del[y]:
            list_check = [0] + list_check
            y += 1
            x = y
            continue

        while x < len(list_check):
            sum_var = (list_in_del[x] + list_check[x]) % 2
            list_in_del[x] = sum_var
            x += 1

        if y == 3:
            break

        list_check = [0] + list_check
        y += 1
        x = y

    list_mod = list_in_del[-3:]  # код вектора остатка
    return list_mod


def make_table(cycle, lst_in):  # печать таблицы
    lst_cycle = [int(x) for x in cycle]
    table = {
        1: {'NK': 0, 'Сочетания': 0, 'CK': 0},
        2: {'NK': 0, 'Сочетания': 0, 'CK': 0},
        3: {'NK': 0, 'Сочетания': 0, 'CK': 0},
        4: {'NK': 0, 'Сочетания': 0, 'CK': 0},
        5: {'NK': 0, 'Сочетания': 0, 'CK': 0},
        6: {'NK': 0, 'Сочетания': 0, 'CK': 0},
        7: {'NK': 0, 'Сочетания': 0, 'CK': 0},
    }  # словарь i-> N0, Сочетания, C0
    mas = make_mas()  # массив от 0b0 до 0b1111111
    for i in mas:
        n = 0                      # cycle = 0b1111111
        tmp = [int(x) for x in i]  # tmp = 0b1111111
        for k in range(len(tmp)):
            if lst_cycle[k] != tmp[k]:
                n += 1  # вычисление количества ошибок

        if n == 0:  # один кодовой вектор без ошибки
            continue

        table[n]['Сочетания'] += 1  # отметка что значение проверено

        err = calc_err(i, 1)  # получения кода ошибки

        if err != [0, 0, 0]:  # попытка исправления
            str_err = ''.join(map(str, err))
            weight_err = dict_err[str_err]
            if tmp[-(weight_err + 1)] == 0:
                tmp[-(weight_err + 1)] = 1
            else:
                tmp[-(weight_err + 1)] = 0
        if lst_in == tmp[0: 4]:
            table[n]['NK'] += 1  # отметка что ошибка исправлена

    for i in table:
        table[i]['CK'] = table[i]['NK'] / table[i]['Сочетания']  # вычисление CK

    df = pd.DataFrame(table)  # печать таблицы (сверху i = [1..7])
    print(df)
    return 0


def make_mas():  # функция создания массива от 0b0 до 0b1111111
    mas_0b = []
    c = 0
    while c < 128:
        tmp_b = bin(c)
        if len(tmp_b[2:]) < 7:
            tmp_b = '0' * (7-len(tmp_b[2:])) + tmp_b[2:]  # добавление недостающих нулей до 7
        else:
            tmp_b = tmp_b[2:]
        mas_0b.append(tmp_b)
        c += 1
    return mas_0b


if __name__ == '__main__':

    in_var = '1101'  # исх циклич код
    lst_in = [int(x) for x in in_var]
    list_cycle = lst_in + calc_err(in_var, 0)  # циклический код

    print('информационный вектор = ', in_var)

    str_list_cycle = ''.join(map(str, list_cycle))
    print('циклический код = ', str_list_cycle)

    make_table(str_list_cycle, lst_in)
