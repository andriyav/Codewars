def smallest(n):
    n_str_list = list(str(n))
    n_int_list = list(map(int, n_str_list))
    print(n)
    k = 0
    for c in range(0, 10):
        len_list = len(n_int_list) - 1
        while len_list > 0:
            f = n_int_list[len_list]
            if n_int_list[len_list] == c:
                n_int_list.pop(len_list)
                n_int_list.insert(0, c)
                k = 1
                break
            len_list -= 1
        if k == 1:
            break
    if n_int_list[0] == 0:
        n_int_list.pop(0)
    indexes = int(''.join(list(map(str, n_int_list))))
    if n_int_list[len_list-1] == c:
        result1 = [len_list, 0 ]
    else:
        result1 = [len_list, 0]
    result1.insert(0, indexes)
    print(result1)


    # метод 2
    n_str_list = list(str(n))
    n_int_list = list(map(int, n_str_list))
    m = 0
    if n_int_list[1] == 0:
        k = n_int_list.pop(0)
        m = 0
        for d in n_int_list:
            if k < d:
                n_int_list.insert(m, k)
                break
            m += 1
    if n_int_list[0] == 0:
        n_int_list.pop(0)
    # result2 = int(''.join(list(map(str, n_int_list))))
    # indexes = [0, m]
    # print(indexes)
    indexes = int(''.join(list(map(str, n_int_list))))
    result2 = [0, m]
    result2.insert(0, indexes)
    print(result2)

    # метод 3
    n_str_list = list(str(n))
    n_int_list = list(map(int, n_str_list))
    deleted_items = []
    while len(n_int_list) > 0:
        min_n = min(n_int_list)
        if min_n >= n_int_list[0]:
            ind = n_int_list.index(min_n)
            f = n_int_list.pop(ind)
            deleted_items.append(f)
        else:
            break
    i = len(n_int_list) - 1
    min_l = min(n_int_list)
    while True: # пошук найменшого другого значення з кінця.
        if n_int_list[i] == min_l:
            print(i)
            break
        i -= 1
    n_int_list.pop(i)
    n_int_list.insert(0, min_l)
    resutlt_list = deleted_items + n_int_list
    ind1 = len(deleted_items)
    if resutlt_list[0] == 0:
        resutlt_list.pop(0)
    # result3 = int(''.join(list(map(str, resutlt_list))))
    # indexes = [i, 0]
    # print(indexes)
    indexes = int(''.join(list(map(str, resutlt_list))))
    result3 = [i+1, ind1]
    result3.insert(0, indexes)
    print(result3)

    # метод 4
    n_str_list = list(str(n))
    n_int_list = list(map(int, n_str_list))
    k = 0
    for c in range(9, 0, -1):
        len_list = len(n_int_list)
        m = 0
        while len_list > m:
            f = n_int_list[m]
            if n_int_list[m] == c:
                n_int_list.pop(m)
                l = len(n_int_list)
                n_int_list.insert(l, c)
                k = 1
                break
            m += 1
        if k == 1:
            break
    if n_int_list[0] == 0:
        n_int_list.pop(0)
    # indexes = [m, l]
    # print(indexes)
    # result4 = int(''.join(list(map(str, n_int_list))))
    indexes = int(''.join(list(map(str, n_int_list))))
    result4 = [m, l]
    result4.insert(0, indexes)
    print(result4)
    print(result1, result2, result3, result4)
    a = [result1, result2, result3, result4]

    print(a)
    a = sorted(a, key=lambda a_entry: a_entry[0])
    print(a)
    result = a[0]
    print(result)
    return result

    # result = min(result1, result2, result3, result4)

    # print(result)

smallest(903723596612970763)
# 254598600046537123 проблема з повторенням нулів. Треба брати перший нуль