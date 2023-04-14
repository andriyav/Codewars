''' Write a function that calculates the least common multiple of its arguments; each argument is assumed
to be a non-negative integer. In the case that there are no arguments (or the provided array in compiled languages
is empty), return 1. If any argument is 0, return 0.'''
import math
def lcm(*args):
    if args == ():
        return 1
    for d in args:
        if d == 0:
            return 0
    # знайдемо Prime factor
    args_prime_factors = []
    args_prime_factors_list = []
    for n in args:
        while n % 2 == 0:
            args_prime_factors.append(2)
            n = n / 2
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                args_prime_factors.append(int(i))
                n = n / i
        if n > 2:
            args_prime_factors.append(int(n))
        args_prime_factors_list.append(args_prime_factors)
        args_prime_factors = []
    args_un = []
    for items in args_prime_factors_list:
        for c in items:
                args_un.append(c)
    args_join_list = args_prime_factors_list[0]
    args_prime_factors_list.pop(0)
    new_args_join_list = args_join_list
    # пошук однакових множників кожного елементу
    for c in args_prime_factors_list:
        for v in c:
            if v in new_args_join_list:
                qty_v = args_join_list.count(v)
                qty_v_prime = c.count(v)
                dif = qty_v - qty_v_prime
                abs_dif = abs(dif)
                if dif < 0:
                    while abs_dif > 0:
                        new_args_join_list.append(v)
                        abs_dif -= 1
            else:
                new_args_join_list.append(v)
    result = 1
    for m in new_args_join_list:
        result *= m
    print(result)
lcm(36, 54, 90)

