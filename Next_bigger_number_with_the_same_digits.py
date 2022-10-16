
def next_bigger(n):
    n_str_list = list(str(n))  # перевід в ліст стрічками
    n_int_list = list(map(int, n_str_list))  # перевід ліст в інтеджер
    n_int_list_muteable = n_int_list.copy()
    range_len = len(n_int_list)
    i = 0
    for i in range(range_len - 2, 0, -1):
        if i + 1 > range_len:
            break
        if n_int_list_muteable[i] < n_int_list_muteable[i + 1]:
            d = n_int_list_muteable[i]
            c = n_int_list_muteable[i + 1:]
            print(d, c)
            break
    f = [b for b in n_int_list_muteable[i + 1:] if n_int_list_muteable[i] < b]
    if f == []:
        if n_int_list_muteable[0] >= n_int_list_muteable[1]:
            print(-1)
            return -1
        else:
            n_int_list_muteable.insert(0, n_int_list[1])
            n_int_list_muteable.pop(2)
            print(n_int_list_muteable)
            result = int(''.join(list(map(str, (n_int_list_muteable)))))
            print(result)
            return result
    else:
        bigger_min = min(f)
        if i != 0:
            index_list_bigger = len(n_int_list) - len(c) + c.index(bigger_min)
        else:
            index_list_bigger = 1
        print(index_list_bigger, 'index_list_bigger')
        print(n_int_list_muteable, '1')
        n_int_list_muteable.insert(i, bigger_min)
        print(n_int_list_muteable, '2')
        s = n_int_list_muteable.pop(i + 1)
        print(n_int_list_muteable,'3', s)
        n_int_list_muteable.insert(index_list_bigger, s)
        print(n_int_list_muteable, '4')
        n_int_list_muteable.pop(index_list_bigger + 1)
        print(n_int_list_muteable, '5')
        list_for_sort = n_int_list_muteable[i+1:]
        list_for_sort.sort()
        print(list_for_sort)
        result = int(''.join(list(map(str, (n_int_list_muteable[:i+1] + list_for_sort)))))
        print(result)
        return result


next_bigger(1123)
# 4252928876459
