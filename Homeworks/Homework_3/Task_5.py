
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

list = []

def negfib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return negfib(n-2) - negfib(n-1)


for i in range(9, 0, -1):
    list.append(negfib(i))



def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


for i in range(1, 9):
    list.append(fib(i))

print(list)
