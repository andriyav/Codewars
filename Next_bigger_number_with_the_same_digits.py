'''Create a function that takes a positive integer and returns the next bigger number
that can be formed by rearranging its digits.'''
def next_bigger(n):
    n_str_list = list(str(n))  # перевід в ліст стрічками
    if len(n_str_list) == 1:
        return -1
    n_int_list = list(map(int, n_str_list))  # перевід ліст в інтеджер
    n_int_list_muteable = n_int_list.copy()
    i = len(n_int_list) - 2
    while i >= 0: #пошук меншого за попередній
        if n_int_list_muteable[i] < n_int_list_muteable[i + 1]:
            c = n_int_list_muteable[i + 1:]
            break
        i -= 1
    if i < 0:
        return -1
    f = [b for b in n_int_list_muteable[i + 1:] if n_int_list_muteable[i] < b]  #пошук більших за меншого за попередній
    bigger_min = min(f) # виділення найбільшого з f
    index_list_bigger = len(n_int_list) - len(c) + c.index(bigger_min) # обмін двох значень
    n_int_list_muteable.insert(i, bigger_min)
    s = n_int_list_muteable.pop(i + 1)
    n_int_list_muteable.insert(index_list_bigger, s)
    n_int_list_muteable.pop(index_list_bigger + 1)
    list_for_sort = n_int_list_muteable[i+1:] # сортування кінця
    list_for_sort.sort()
    result = int(''.join(list(map(str, (n_int_list_muteable[:i+1] + list_for_sort)))))  # конкатинація сортованого та решта
    return result

next_bigger(4252928876459)

