import math
a, b, c = float(input()), float(input()), float(input())
D = math.pow(b, 2) - 4 * a * c
if D > 0:
    x1 = (-b - math.sqrt(D)) / (2 * a)
    x2 = (-b + math.sqrt(D)) / (2 * a)
    if x1 > x2:
        print(x2, x1, sep='\n')
    else:
        print(x1, x2, sep='\n')
elif D == 0:
    x = -b / (2 * a)
    print(x)
else:
    print('Нет корней')