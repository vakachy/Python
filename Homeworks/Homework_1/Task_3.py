# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0
# и выдаёт номер четверти плоскости, в которой находится эта точка (или какой оси принадлежит).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = float(input("Enter x: "))
y = float(input("Enter y: "))

if ((x != 0) or (y != 0)):

    if (x > 0 and y > 0):
        print(f"({x},{y}) --> 1-st Quadrant")
    elif (x < 0 and y > 0):
        print(f"({x},{y}) --> 2-nd Quadrant")
    elif (x < 0 and y < 0):
        print(f"({x},{y}) --> 3-rd Quadrant")
    elif (x > 0 and y < 0):
        print(f"({x},{y}) --> 4-th Quadrant")
    elif (x == 0 and (y > 0 or y < 0)):
        print(f"({x},{y}) --> belongs to Y-axis")
    elif ((x > 0 or x < 0) and y == 0):
        print(f"({x},{y}) --> belongs to X-axis")

else:
    print("x and y must not both equal zero")
