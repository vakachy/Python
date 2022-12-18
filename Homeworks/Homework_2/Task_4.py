
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в отдельном списке
# Пример n=4, lst1=[-4,-3,-2,0,1,2,3,4] - список на основе n, а позиции элементов lst2=[3,1].

n = int(input("Enter natural N: "))

l1 = list()

for i in range(-n, n+1):
    l1.append(i)
print(l1)

l2 = [3, 1]

mult = 1

for i in l2:
    mult *= l1[i]

print(f"Result of multiplication of elements of l1={l1} @ positions of l2={l2}: {mult}")