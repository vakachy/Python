
# Реализуйте алгоритм перемешивания списка (рандомно поменять местами элементы списка между собой).

import random

####### Variant 1 #######

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("####### Initial list #######")
print(l1)
random.shuffle(l1)
print("####### Variant 1 #######")
print(l1)

####### Variant 2 #######

l2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

index = 0

for i in range(len(l2)-1):
    index = random.randint(i+1, len(l2)-1)

    l2[i], l2[index] = l2[index], l2[i]

print("####### Variant 2 #######")
print(l2)
