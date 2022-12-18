
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

t = input("Enter a real number N: ")
sum = 0

for i in t:
    if (i != '.' and i != ',' and i != '-' and i != '+'):
        sum += int(i)
print(f'Sum of numbers of N: {sum}')
