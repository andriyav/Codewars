import re


def simplify(poly):
    poly_sorted = []
    pattern = r'(\W+)'
    pol_split = re.split(pattern, poly)
    for i in pol_split:
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
        k = 0
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
    for a in poly_with_sign:  # знайдемо унікальні елементи
        pattern = r'([a-z]+)'
        f = re.findall(pattern, a)
        if f[0] not in unique:
            unique.append(f[0])
    sort_item_list = []
    sort_item_list_total = []
    number = 0
    k = 0
    for b in unique:
        for c in poly_with_sign:  # сортування по поліномам
            pattern = r'([a-z]+)'
            xy = re.findall(pattern, c)
            pattern = r'(\d+)'
            dig = re.findall(pattern, c)
            if dig == []:
                dig = [1]
            if b == xy[0]:
                sort_item_list.append(poly_with_sign[k])
                k += 1
        sort_item_list_total.append(sort_item_list)
        sort_item_list = []
    result = ''
    sum_str = ''
    for l in sort_item_list_total:  # сумування поліномів та числових значень
        sum = 0
        for m in l:
            pattern = r'([a-z]+)'
            xy = re.findall(pattern, m)
            pattern = r'(-?\d+)'
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
        total = sum_str + xy[0]
        result += total
    print(result)
    # вирішити пробоему стосовно наявності "+", та видалення полінома у випадку числового інтексу рівного нулю


simplify("-100xt-22tx+2er")
# for d in multy_total:
# memory error to many elements


#     if poly_sorted[0] == '':
#         poly_sorted.pop(0)
# for char in poly_sorted:
#     if not char[0].isdigit() and not char[0] == '-' and not char[0] == '+':
#         char = '1' + char
#         poly_sorted.pop(k)
#         poly_sorted.insert(k, char)
#     pattern = r'(\d+)'
#     dig = re.findall(pattern, char)
#     for i in char:
#         if i.isdigit():
#             pattern = r'(\d+)'
#             dg = re.findall(pattern, char)
#             pattern = r'(\D+)'
#             xy = re.findall(pattern, char)
#             if_minus = poly_sorted[k-1]
#             if if_minus == '-':
#                 mult_xy_minus = ['-' + xy[0]]
#                 mult_xy = mult_xy_minus * int(dg[0])
#             else:
#                 mult_xy = xy * int(dg[0])
#             print(xy[0])
#             index_char = poly_sorted.index(xy[0])
#             poly_sorted.pop(index_char)
#             for c in mult_xy:
#                 poly_sorted.insert(index_char, c)
#     k += 1
#     poly_without_minus = []
# for n in poly_sorted:
#     if n != '-' and n != '+':
#         poly_without_minus.append(n)
#         n = 1
#         sort_list = []
#         sort_without_minus = []
# for x in poly_without_minus:
#     if x[0] == '-':
#         item = x[1:]
#     else:
#         item = x
#     sort_without_minus.append(item)
# unieuq = []
# for g in sort_without_minus:
#     if g not in unieuq:
#         unieuq.append(g)
# d = 1
# sort_types = []
# sorted_types = []
# for m in unieuq:
#     for k in poly_without_minus:
#         if k[0] == '-':
#             item = k[1:]
#         else:
#             item = k
#         if m == item:
#             sort_types.append(k)
#     if sort_types != []:
#         sorted_types.append(sort_types)
#     sort_types = []
#     minus_number = 0
#     count_list = []

# sorted_types = sorted(sorted_types, key=len, reverse=True)
# for item_list in sorted_types:
#     for minus_count in item_list:
#         if minus_count[0] != '-':
#             minus_number += 1
#         else:
#             minus_number -= 1
#     if minus_number != 0:
#         if minus_number == 1:
#             str_numebr = ''
#         elif minus_number == -1:
#             str_numebr = '-'
#         else:
#             str_numebr = str(minus_number)
#         if minus_count[0] == '-':
#             concatinate_xy = minus_count[1:]
#         else:
#             concatinate_xy = minus_count
#         count_list.append(str_numebr + concatinate_xy)
#         minus_number = 0