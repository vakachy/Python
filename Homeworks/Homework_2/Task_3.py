
# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

l = list()
sum = 0

n = int(input("Enter N: "))


for i in range(1, n+1):
    l.append(round((1+1/i)**(i), 3))

for i in l:
    sum += i

# print(l)
print(f"Sum of the first {n} items of the given series (1+1/n)**n: {sum}")
