def smallest(n):
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
            break
        i -= 1
    n_int_list.pop(i)
    n_int_list.insert(0, min_l)
    len_del = len(deleted_items)
    resutlt_list = deleted_items + n_int_list
    if resutlt_list[0] == 0:
        resutlt_list.pop(0)
    result = int(''.join(list(map(str, resutlt_list))))
    if len(str(result)) != len(str(n)) and str(n)[1] == '0':
        result = [result, len_del, (i + len_del)]
    else:
        result = [result, (i+len_del), len_del]


    print(result)

smallest(269045)