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
    poly_with_sign = []
    n = 0
    print(poly_sorted, 'poly_sorted')
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
    print(poly_with_sign, 'poly_with_sign')
    if poly_with_sign[0] == '':
        poly_with_sign.pop(0)
    for a in poly_with_sign:  # знайдемо унікальні елементи
        pattern = r'([a-z]+)'
        f = re.findall(pattern, a)
        if f[0] not in unique:
            unique.append(f[0])
    sort_item_list = []
    sort_item_list_total = []
    for b in unique:
        k = 0
        for c in poly_with_sign:  # сортування по поліномам
            pattern = r'([a-z]+)'
            xy = re.findall(pattern, c)
            pattern = r'([-+]\d+)'
            dig = re.findall(pattern, c)
            if b == xy[0]:
                sort_item_list.append(poly_with_sign[k])
            k += 1
        sort_item_list_total.append(sort_item_list)
        sort_item_list = []
        print(sort_item_list_total, 'sort_item_list_total')
        # xy_dig_sighn = []
        # xy_dig_sighn_total = []
    # for x in sort_item_list_total:
    #     pattern = r'([a-z]+)'
    #     xy = re.findall(pattern, x[0])
    #     pattern = r'(\d+)'
    #     dig = re.findall(pattern, x[0])
    #     pattern = r'([-+])'
    #     sighn = re.findall(pattern, x[0])
    #     print(xy, dig, sighn, 'xy dig sign')
    #     if xy != []:
    #         xy_dig_sighn.append(xy[0])
    #     if dig != []:
    #         xy_dig_sighn.append(dig[0])
    #     if sighn != []:
    #         xy_dig_sighn.append((sighn[0]))
    #     xy_dig_sighn_total.append(xy_dig_sighn)
    #     xy_dig_sighn = []
    # xy_dig_sighn_total.sort()
    # print(xy_dig_sighn_total, 'xy_dig_sighn_total')
    # s = ''
    # xy_dig_sighn_sorted = []
    # for n in xy_dig_sighn_total:
    #     for z in n:
    #         s = z + s
    #
    #
    #     xy_dig_sighn_sorted.append([s])
    #     s = ''
    # print(xy_dig_sighn_sorted, 'sorted')

    result = ''
    f_list_total = []
    d_list_total = []
    list_sort = []

    print(sort_item_list_total, 'sort_item_list_total')
    # sort_item_list_total = xy_dig_sighn_sorted #-----------------------------------------------------
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
    print(d_list_total, 'total')
    for i in d_list_total:
        if i[0][0] in '234567890':
            d_list_total = sorted(d_list_total, reverse=True)
            break
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
            print(dig)
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
        list_for_sorting.sort()
        list_for_sorting.append([total])
        print(list_for_sorting, 'list_for_sorting')
        result += total
    for v in list_for_sorting:  # відсортовано, в незалжності від знака
        pattern = r'([a-z]+)'
        xy = re.findall(pattern, v[0])
        pattern = r'([-+]*\d*)'
        dig = re.findall(pattern, v[0])
        if dig == []:
            dig = ['']
        list_v = [xy[0], dig[0]]
        list_sort.append(list_v)
        list_sort.sort()
    concat_list = []
    for j in list_sort:
        concat_j = j[1] + j[0]
        concat_list.append([concat_j])
    result2 = ''
    for p in concat_list:
        result2 += p[0]
    if result2[0] == '+':
        result2 = result2[1:]
    if result[0] == '+':
        result = result[1:]
    print(result2, 'result2')
    print(result, 'result1')
    list_sort_str = []
    for n in list_for_sorting:
        list_sort_str.append(n[0])
    list_sort_str.sort(key=len)
    print(list_sort_str, 'list_sort_str')
    total_3 = ''
    for s in list_sort_str:
        total_3 += s
    print(total_3, 'total3')
    for i in result:  # вибір сортування "-abc+3a+2ac" або  y-x
        if i in '1234567890':
            break
        else:
            for c in list_sort_str:  # вибір сортування xyz-xz
                if len(list_sort_str[0]) == len(c):
                    result = result2
                else:
                    result = total_3
                    break
    if result[0] == '+':
        result = result[1:]
    print(result)
    return (result)


# зробити сортування за a+ca-ab

simplify("a+2ca-3ab")
