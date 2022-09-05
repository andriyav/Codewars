import re


def simplify(poly):
    poly_sorted = []
    pattern = r'(\W+)'
    pol_split = re.split(pattern, poly)
    for i in pol_split:
        i_joined = list(''.join(i))
        i_sorted = sorted(i_joined)
        i_split = ''.join(i_sorted)
        poly_sorted.append(i_split)
        mult_xy = ''
        k = 0
        if poly_sorted[0] == '':
            poly_sorted.pop(0)
    for char in poly_sorted:
        if not char[0].isdigit():
            char = '1' + char
            poly_sorted.pop(k)
            poly_sorted.insert(k, char)
        pattern = r'(\d+)'
        dig = re.findall(pattern, char)
        print(dig)
        for i in char:
            if i.isdigit():
                pattern = r'(\D+)'
                xy = re.findall(pattern, char)
                if_minus = poly_sorted[k - 1]
                if if_minus == '-':
                    mult_xy_minus = ['-' + xy[0]]

                    # проблема із більшою кількістю цифр на початку

                    mult_xy = mult_xy_minus * int(dig[0])

                else:
                    mult_xy = xy * int(dig[0])
    #             index_char = poly_sorted.index(char)
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
    # print(sorted_types)
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
