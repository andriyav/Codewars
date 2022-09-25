def smallest(n):
    n_str_list = list(str(n))
    n_int_list = list(map(int, n_str_list))
    min_n = min(n_int_list)
    print(min_n)


smallest(2633335)