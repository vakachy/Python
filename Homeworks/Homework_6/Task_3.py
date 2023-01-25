

# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

l = [1, 5, 3, 3, 2, 4, 4, 2, 5, 5, -10]

# ------------------------------------------------------ #
# первый вариант решения (уникальные значения)


l = sorted(l)
l1 = []

i = 0
while (i < len(l)):
    count = l.count(l[i])
    if (count > 1):
        i += count
    else:
        l1.append(l[i])
        i += 1

print(l1)
# ------------------------------------------------------ #
# второй вариант решения (уникальные значения)


from random import randint
 
array_int = l
new_array = [item for item in array_int if array_int.count(item) == 1]

print(new_array)
# ------------------------------------------------------ #
# первый вариант решения (!НЕ уникальные значения!)


a= l
print(set(a))
# ------------------------------------------------------ #
# второй вариант решения (!НЕ уникальные значения!)


l1=[]
for i in l:
    if i not in l1: l1.append(i)

print('l1 = ', l1)