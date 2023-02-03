
# Программа для вычисления числа π из домашнего задания к Семинару №4
# с добавлением шкалы прогресса progress bar
# Вычислить число π c заданной точностью d

# Пример:

# - при d = 0.001, π = 3.141.   10^{-1} ≤ d ≤10^{-10}
# π = 3.1415926535897932384626433832795

# from time import sleep
from light_progress import ProgressBar

def calc_pi(d='0.001'):
    # точность округления числа π (задается как аргумент функции, по умолчанию d=0.001)
    d = len(d[d.index('.') + 1:])


# количество итераций для вычисления числа π
    tolerance = 100000000
# длина шкалы progress bar:
    scale_length = 100
# количество итераций цикла, приходящихся на один шаг шкалы progress bar:
    step = tolerance // scale_length

    progress_bar = ProgressBar(scale_length)
    progress_bar.start()
# цикл вычисления числа π
    # π вычисляется, если точность округления d в допуске
    # вычисление по формуле Лейбница (очень медленная сходимость)
    if (1 <= d <= 10):
        k = 1
        sum = 0.0
        for i in range(tolerance):            
            if i % 2 == 0:
                sum += 4 / k
            else:
                sum -= 4 / k
            k += 2
# если i кратно step, то сдвигается шкала progress bar:
            if i % step == 0:
                progress_bar.forward()
        progress_bar.finish()
        return round(sum, d)
# если d не в допуске, то выводится сообщение об этом
    else:
        progress_bar.finish()
        return 'Warning!\nd out of range: 10^(-1)<=d<=10^(-10)'

print(calc_pi('0.1'))
print(calc_pi())
print(calc_pi('0.0000000001'))
print(calc_pi('0.000000000001'))
