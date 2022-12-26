
# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input("Enter a natural degree of polynomial k = "))

t = []

for i in range(k, -1, -1):
    coef = random.randint(0, 101)

    if (coef == 0):
        continue

    elif (coef == 1):
        if (i == 0):
            t.append(f'{coef}')
        elif (i == 1):
            t.append(f'x')
        else:
            t.append(f'x^{i}')

    else:
        if (i == 0):
            t.append(f'{coef}')
        elif (i == 1):
            t.append(f'{coef}*x')
        else:
            t.append(f'{coef}*x^{i}')


s = ''
for i in range(len(t)):
    if (i < len(t)-1):
        s += f'{t[i]} + '
    else:
        s += f'{t[i]}'


with open('Homework_4,Task_4.txt', 'w') as f:
    f.write(s)
