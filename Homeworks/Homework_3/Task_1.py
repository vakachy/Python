
# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

c = int(input("Enter a number of items in a list: "))
l = list()
mult = 1

for i in range(c):
    l.append(random.randint(0, 5*c))

print(l)

for i in range(len(l)):
    if (i % 2 == 0):
        mult *= l[i]

print(f"Result of multiplication of odd items of the list {l} is: {mult}")