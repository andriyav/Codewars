import math
def tub_function():
    a = float(input('Введіть значення а'))
    while a <= 0:
        a = float(input("Значення може бути тільки позитивним. Спробуйте ще раз:"))
    b = float(input('Введіть значення b'))
    while b <= 0:
        b = float(input("Значення може бути тільки позитивним. Спробуйте ще раз:"))
    n = int(input('Введіть значення n'))
    while n <= 0:
        n = float(input("Значення може бути тільки позитивним. Спробуйте ще раз:"))
    h = (b - a) / n
    for i in range(0, n+1):
        x = a + i * h
        result = 2 * (x ** 2) + math.log(x)
        print('f(x) =', result, 'при a =', a, 'b=', b, 'i =', i)

tub_function()