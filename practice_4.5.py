# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

new_list = [i for i in range(100, 1001, 2)]


def my_func(prev_el, el):
    return prev_el * el


print(reduce(my_func, new_list))


# Решение через цикл
def while_sum(num_list):
    i = 0
    while i + 1 < len(num_list):
        new_el = num_list[i]
        for el in range(len(num_list) - 1):
            new_el = new_el * num_list[i + 1]
            i += 1
    return new_el


print(while_sum(new_list))
