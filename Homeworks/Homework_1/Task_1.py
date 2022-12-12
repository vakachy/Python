# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет


day = int(input('Enter the number of the weekday: '))

while (day not in range(1, 8)):
    print('Out of range!')
    day = int(input('Enter the number of the weekday (1 to 7): '))
else:
    if (day < 6):
        print('No')
    else:
        print('Yes')
