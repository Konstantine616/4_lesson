# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import (count,
                       cycle,
                       )

from random import randint


def int_gen():
    while True:
        a = input('Введите число с которого начнется отсчет:\n')
        if a.isdigit():
            a = int(a)
            break
        else:
            print('Ошибка ввода.')

    while True:
        b = input('Введите число с которого начнется отсчет:\n')
        if b.isdigit():
            b = int(b)
            break
        else:
            print('Ошибка ввода.')

    for el in count(a):
        if el <= b:
            print(el)
        else:
            break


def cycle_list():
    new_list = [randint(1, 99) for _ in range(randint(4, 11))]
    iter_cycle = cycle(new_list)
    print('\n', new_list)
    while True:
        exit = input('Для перемещения по списку нажмите ENTER, для завершения программы введите любой символ:')
        if exit == '':
            print(new_list)
            print(next(iter_cycle))
        else:
            return


int_gen()
cycle_list()
