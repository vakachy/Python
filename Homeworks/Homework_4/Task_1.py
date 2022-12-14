
# Вычислить число π c заданной точностью d

# Пример:

# - при d = 0.001, π = 3.141.   10^{-1} ≤ d ≤10^{-10}
# π = 3.1415926535897932384626433832795

####### Variant 1 #######

def calc_pi_1(d='0.001'):

    d = len(d[d.index('.')+1:])

# если точность d в допуске, то вычисляется π по формуле Лейбница (очень медленная сходимость)

    if (1 <= d <= 10):
        k = 1
        sum = 0.0

        for i in range(10000000):
            if i % 2 == 0:
                sum += 4/k
            else:
                sum -= 4/k
            k += 2

        return round(sum, d)

# если d не в допуске, то выводится сообщение об этом

    else:
        return 'd out of range: 10^(-1)<=d<=10^(-10)'


print(calc_pi_1('0.1'))
print(calc_pi_1())
print(calc_pi_1('0.0000000001'))
print(calc_pi_1('0.000000000001'))

####### Variant 2 #######


def calc_pi_2(d='0.001'):
    d = len(d[d.index('.')+1:])

# если точность d в допуске, то вычисляется π по формуле
# π=3+4/(2·3·4)-4/(4·5·6)+4/(6·7·8)-4/(8·9·10)+4/(10·11·12)-4/(12·13·14)...

    if (1 <= d <= 10):

        n = 1
        s = 3.0

        for i in range(0, 2000):
            n = (2*i+2)*((2*i)+3)*((2*i)+4)

            if (i % 2 != 0):
                s -= 4/n

            else:
                s += 4/n
        return round(s, d)

# если d не в допуске, то выводится сообщение об этом

    else:
        return 'd out of range: 10^(-1)<=d<=10^(-10)'


print(calc_pi_2('0.1'))
print(calc_pi_2())
print(calc_pi_2('0.0000000001'))
print(calc_pi_2('0.000000000001'))
