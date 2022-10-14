# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
from functools import reduce


def get_user_number(str_1):
    while True:
        try:
            num = int(input(str_1))
            return num
        except ValueError:
            print("Вы ввели не целое число. Повторите ввод")


def get_user_random_list(arr_len):
    # arr_list = []
    # for i in range(arr_len):
    #     arr_list.append(random.randint(0, 10))
    # print(arr_list)
    return [randint(0, 10) for i in range(arr_len)]


def get_sum_odd_position(arr):
    # sum_odd_position = 0
    # for i in range(user_len):
    #     if i % 2 != 0:
    #         sum_odd_position += arr[i]
    sum_odd_position = reduce(lambda sum, x: sum + x, arr[1::2], 0)
    print(
        f'Cуммa элементов списка, стоящих на нечётной позиции: {sum_odd_position}')


user_len = get_user_number('Задайте длину списка (массива): ')
user_list = get_user_random_list(user_len)
print(user_list)
get_sum_odd_position(user_list)
