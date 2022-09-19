import math
def lcm(*args):
    for d in args:
        if d == 0:
            return 0
    args_prime_factors = []
    args_prime_factors_list = []
    for n in args:
        while n % 2 == 0:
            args_prime_factors.append(2)
            n = n / 2

        # n must be odd at this point
        # so a skip of 2 ( i = i + 2) can be used
        for i in range(3, int(math.sqrt(n)) + 1, 2):

            # while i divides n , print i and divide n
            while n % i == 0:
                args_prime_factors.append(int(i))
                n = n / i

        # Condition if n is a prime
        # number greater than 2
        if n > 2:
            args_prime_factors.append(int(n))
        args_prime_factors_list.append(args_prime_factors)
        args_prime_factors = []
    print(args_prime_factors_list, 'args_prime_factors_list')
    args = args_prime_factors_list
    zip_args_prime_factor = list(zip(*args))
    least_len_list = []
    for len_item in args_prime_factors_list:
        least_len_list.append(len(len_item))
        least_len = min(least_len_list)
        rest_items = []
    for d in args_prime_factors_list:
        if len(d) > least_len:
                rest_items.append(d[least_len:])

    print(rest_items, 'rest_items_factor')
    print(zip_args_prime_factor, 'zip_args_prime_')
    set_list = []
    for a in zip_args_prime_factor:
        set_list.append(set(a))
    print(set_list)
    total_set =set_list + rest_items
    print(total_set)
    total_set_in_one_row = []
    mult_set = 1
    for d in total_set:
        for c in d:
            mult_set *= c
            total_set_in_one_row.append(c)
    print(total_set_in_one_row)
    print(mult_set)
    return mult_set


# Zip не підходить







lcm(7, 35)