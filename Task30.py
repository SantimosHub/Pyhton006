# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

start_number = int(input('Ввведите начало арифметической прогрессии: '))
count_number = int(input('Ввведите колличество элементов: '))
step_number = int(input('Ввведите шаг прогрессии: '))

progres_list = []

for i in range(0, count_number):
    progres_list.append(start_number)
    start_number += step_number

print(progres_list)
