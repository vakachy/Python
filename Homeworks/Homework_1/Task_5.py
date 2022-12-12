# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

print("Enter coordinates of point A(xa, ya)")
xa = float(input("Enter xa: "))
ya = float(input("Enter ya: "))
print("Enter coordinates of point B(xb, yb)")
xb = float(input("Enter xb: "))
yb = float(input("Enter yb: "))

distance =  ((xa-xb)**2 + (ya-yb)**2)**0.5
distance = round(distance,3)
print(f"A({xa},{ya}); B({xb},{yb}) --> {distance}")