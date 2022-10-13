from copy import copy
from unittest import result


def next_bigger(n):
    n_str_list = list(str(n))  # перевід в ліст стрічками
    n_int_list = list(map(int, n_str_list))  # перевід ліст в інтеджер
    n_int_list_muteable = n_int_list.copy()
    range_len = len(n_int_list)
    min_list = n_int_list_muteable.copy()
    result6 = []
    max_list = n ** 2
    #  переміщенні кожної цифри з ліва на право

    for g1 in range(range_len - 1, 0, -1):
        n_int_list_muteable = n_int_list.copy()
        c = 0
        for g2 in range(range_len - 1, 0, -1):
            n_int_list_muteable.insert(g1 + 1 + c, n_int_list[g1 - 1])
            c += 1
            n_int_list_muteable.pop(g1 + c - 2)
            if int(''.join(list(map(str, n_int_list_muteable)))) > n:  # зі всього переліку залишається найменше число
                d = int(''.join(list(map(str, n_int_list_muteable))))
                if d < max_list:
                    max_list = int(''.join(list(map(str, n_int_list_muteable))))

            if g1 + c >= range_len:
                break
    result1 = max_list
    print(result1)

    g = 0
    max_list = n ** 2
    for g1 in range(range_len, -1, -1):
        n_int_list_muteable = n_int_list.copy()
        for g2 in range(range_len, 1 + g, -1):
            n_int_list_muteable.insert(g2 - 2 - g, n_int_list[g1 - 1])
            n_int_list_muteable.pop(g2 - g)
            if int(''.join(list(map(str, n_int_list_muteable)))) > n:
                d = int(''.join(list(map(str, n_int_list_muteable))))
                if d < max_list:
                    max_list = int(''.join(list(map(str, n_int_list_muteable))))

        g += 1
    result2 = max_list
    print(result2)
    result = max([result1, result2])
    print(result)


next_bigger(895728512)
# 1234567908
