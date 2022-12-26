
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("Enter N: "))


def isPrime(n):
    if (n == 1 or n == 2):
        return 1
    elif (n <= 0):
        return 0
    else:
        for i in range(2, n):
            if (n % i == 0):
                return 0
        else:
            return 1


l = []

for i in range(n+1):
    if (isPrime(i)):
        if (n % i == 0):
            l.append(i)

print(f'Prime unique factors of N={n} are/Уникальные простые делители числа N={n}: {l}')


i = 0
t = []

while (n != 1):
    if (i > len(l)-1):
        i = 1
    else:
        if (n % l[i] == 0):
            n //= l[i]
            t.append(l[i])
            i += 1
        else:
            i += 1

print(f'All the prime factors of N={n} are/Все простые делители числа N={n}: {sorted(t)}')
