# Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных координат точек в этой четверти (x и y).

x = int(input("Enter quadrant number: "))

if (x == 1):
    print("x>0 and y>0")
elif(x==2):
    print("x<0 and y>0")
elif(x==3):
    print("x<0 and y<0")
elif(x==4):
    print("x>0 and y<0")
    