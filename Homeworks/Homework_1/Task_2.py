# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print("Assume that, for example: X < 0, Y < 0, Z < 0")
print("Enter values of X, Y, Z to check statement: ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z")

x = float(input("Enter X: "))
x = x < 0
if (x):
    print("X<0", f'X={x}')
else:
    print("X>0", f'X={x}')


y = float(input("Enter Y: "))
y = y < 0
if (y):
    print("Y<0", f'Y={y}')
else:
    print("Y>0", f'Y={y}')


z = float(input("Enter Z: "))
z = z < 0
if (z):
    print("Z<0", f'Z={z}')
else:
    print("Z>0", f'Z={z}')

print(f'Have,\nX = {x}, Y = {y}, Z = {z}')
print("Next, got that:")
print(f'1) ¬(X ⋁ Y ⋁ Z) = ¬({x} ⋁ {y} ⋁ {z}) = {not (x and y and z)}')
print(f'2) (¬X ⋀ ¬Y ⋀ ¬Z) = (¬{x} ⋀ ¬{y} ⋀ ¬{z}) = {(not (x) or not (y) or not (z))}')

print('So,:', end=" ")
if (not (x and y and z) == (not (x) or not (y) or not (z))):
    print('¬(X ⋁ Y ⋁ Z) == (¬X ⋀ ¬Y ⋀ ¬Z)')
    print("Statement proved to be equality\nEnd")
else:
    print('¬(X ⋁ Y ⋁ Z) != (¬X ⋀ ¬Y ⋀ ¬Z)')
    print("Statement not proved to be equality\nEnd")

