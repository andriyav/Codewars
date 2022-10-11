def next_bigger(n):
    n_str_list = list(str(n))  # перевід в ліст стрічками
    n_int_list = list(map(int, n_str_list))  # перевід ліст в інтеджер
    n_int_list_muteable = n_int_list.copy()
    range_len = len(n_int_list)
    min_list = n_int_list_muteable.copy()
    result6 = []
    #  переміщенні кожної цифри з ліва на право
    for g1 in range(0, range_len):
        n_int_list_muteable = n_int_list.copy()
        for g2 in range(2, range_len + 1):
            n_int_list_muteable.insert(g2 + g1, n_int_list[g1])
            n_int_list_muteable.pop(g2 + g1 - 2)
            if int(''.join(list(map(str, n_int_list_muteable)))) > int(
                    ''.join(list(map(str, min_list)))) :  # зі всього переліку залишається найменше число
                min_list = int(''.join(list(map(str, n_int_list_muteable))))
                print(min_list)
                return(min_list)
            if g1 + g2 >= range_len:
                break

    g = 0
    for g1 in range(range_len, -1, -1):
        n_int_list_muteable = n_int_list.copy()
        for g2 in range(range_len, 1 + g, -1):
            n_int_list_muteable.insert(g2 - 2 - g, n_int_list[g1 - 1])
            n_int_list_muteable.pop(g2 - g)
            if int(''.join(list(map(str, n_int_list_muteable)))) > n:
                max_list = int(''.join(list(map(str, n_int_list_muteable))))
                print(max_list)
                return max_list
        g += 1
    print(-1)
    return -1

next_bigger(1234567890)
# 1234567908
