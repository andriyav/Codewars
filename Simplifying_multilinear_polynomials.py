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
        k = 0
        if poly_sorted[0] == '':
            poly_sorted.pop(0)
    for char in poly_sorted:
        if not char[0].isdigit():
            char = '1' + char
            poly_sorted.pop(k)
            poly_sorted.insert(k, char)
        for i in char:
            if i.isdigit():
                pattern = r'(\D+)'
                xy = re.findall(pattern, char)
                if_minus = poly_sorted[k-1]
                if if_minus == '-':
                    mult_xy_minus = ['-' + xy[0]]
                    mult_xy = mult_xy_minus * int(i)
                else:
                    mult_xy = xy * int(i)
                index_char = poly_sorted.index(char)
                poly_sorted.pop(index_char)
                for c in mult_xy:
                    poly_sorted.insert(index_char, c)
        k += 1
        poly_without_minus = []

    for n in poly_sorted:
        if n != '-' and n != '+':
            poly_without_minus.append(n)
    print(poly_without_minus)
    separate_in = []
    total_separate = []
    k = 0
    for x in poly_without_minus:
        for y in poly_without_minus:
            if x[0] == '-':
                x_abs = x[1:]
                if y[0] == '-':
                    y_abs = y[1:]
                    if x_abs == y_abs:
                        separate_in.append(x)
                        k += 1
                    else:
                        if separate_in != []:
                            total_separate.append(separate_in)

    separate_in = []
    total_separate_min = []
    k = 0
    # for x in poly_without_minus:
    #     for y in poly_without_minus:
    #         if x[0] != '-':
    #             x_abs = x
    #             if y[0] != '-':
    #                 y_abs = y
    #                 if x_abs == y_abs:
    #                     separate_in.append(x)
    #                     k += 1
    #                 else:
    #                     if separate_in != []:
    #                         total_separate_min.append(separate_in)
    #                         separate_in = []
    #         else: break

    print(total_separate)
    # print(total_separate_min)



    # for v in poly_without_minus:
    #     if v[0] != '-':
    #         pattern = r'(\w+)'
    #         xy = re.findall(pattern, v)
    #         print(xy)

simplify("-3xy+3yx-3cd-dc+we")
