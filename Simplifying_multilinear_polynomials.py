# Write a function: simplify, that takes a string in input, representing a multilinear non-constant polynomial in integers coefficients (like "3x-zx+2xy-x"), and returns another string as output where the same expression has been simplified in the following way ( -> means application of simplify):
#     All possible sums and subtraction of equivalent monomials ("xy==yx") has been done, e.g.:
#     "cb+cba" -> "bc+abc", "2xy-yx" -> "xy", "-a+5ab+3a-c-2a" -> "-c+5ab"

import re
def simplify(poly):
    poly_sorted = []
    pattern = r'(\W+)'
    pol_split = re.split(pattern, poly)
    for i in pol_split:   # Розбиття на знак, цифру, поліном
        pattern = r'(\D+)'
        cb = re.findall(pattern, i)
        i_joined = list(''.join(cb))
        i_sorted = sorted(i_joined)
        i_split = ''.join(i_sorted)
        pattern = r'(\d+)'
        digi = re.findall(pattern, i)
        digi.append(i_split)
        digi = ''.join(digi)
        poly_sorted.append(digi)
    poly_with_sign = []
    n = 0
    while len(poly_sorted) > n:  # приведем знаки до відповідного елементу
        if poly_sorted[n] == '-':
            item = '-' + poly_sorted[n + 1]
            n += 1
        elif poly_sorted[n] == '+':
            item = poly_sorted[n + 1]
            n += 1
        else:
            item = poly_sorted[n]
        n += 1
        poly_with_sign.append(item)
    unique = []
    if poly_with_sign[0] == '':
        poly_with_sign.pop(0)
    for a in poly_with_sign:  # знайдемо унікальні елементи та відсуртуємо за довжиною та алфавітом
        pattern = r'([a-z]+)'
        f = re.findall(pattern, a)
        if f[0] not in unique:
            unique.append(f[0])
    unique = sorted(unique, key=lambda x: (len(x), x))
    sort_item_list = []
    sort_item_list_total = []
    for b in unique:
        k = 0
        for c in poly_with_sign:  # сортування по поліномам
            pattern = r'([a-z]+)'
            xy = re.findall(pattern, c)
            if b == xy[0]:
                sort_item_list.append(poly_with_sign[k])
            k += 1
        sort_item_list_total.append(sort_item_list)
        sort_item_list = []
    result = ''
    f_list_total = []
    d_list_total = []
    for d in sort_item_list_total:
        for f in d:
            if f[0].isalpha():
                list_f = list(f)
                list_f.insert(0, '1')
                list_f = ''.join(list_f)
                f_list_total.append(list_f)
            elif f[0] == '-' and f[1] not in '1234567890':
                list_f = list(f)
                list_f.insert(1, '1')
                list_f = ''.join(list_f)
                f_list_total.append(list_f)
            elif f[1] in '1234567890':
                list_f = list(f)
                list_f = ''.join(list_f)
                f_list_total.append(list_f)
            elif f[0] in '1234567890':
                list_f = list(f)
                list_f = ''.join(list_f)
                f_list_total.append(list_f)
        d_list_total.append(f_list_total)
        f_list_total = []
    list_for_sorting = []
    for l in d_list_total:  # сумування поліномів та числових значень
        sum = 0
        for m in l:
            pattern = r'([a-z]+)'
            xy = re.findall(pattern, m)
            pattern = r'(^[\-\+]?\d*)'
            dig = re.findall(pattern, m)
            if dig == []:
                dig = ['1']
            elif dig == ['-']:
                dig = ['-1']
            sum += int(dig[0])
        if sum == -1:
            sum_str = '-'
        elif sum == 1:
            sum_str = ''
        else:
            sum_str = str(sum)
        if sum < 0:
            total = sum_str + xy[0]
        elif sum == 0:
            continue
        else:
            total = "+" + sum_str + xy[0]
        list_for_sorting.append([total])
        result += total
    if result[0] == '+':
        result = result[1:]
    return result

simplify("a+2ca-3ab")
