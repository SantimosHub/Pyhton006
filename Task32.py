# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

list_lenght = int(input('Ввведите длину массива: '))
min_num = int(input('Ввведите начало диапазона: '))
max_num = int(input('Ввведите конец диапазона: '))

rand_list = [randint(-50, 50) for i in range(0, list_lenght)]
index_list = []

for i in range(0, list_lenght):
    if min_num <= rand_list[i] <= max_num:
        index_list.append(i)

print(rand_list)
print(index_list)
