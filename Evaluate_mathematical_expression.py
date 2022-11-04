
import re


def correction(expression):
    expression_list = list(expression)
    k = 0
    n = 0
    while len(expression_list) - 1 > k:
        a = expression_list[k]
        b = expression_list[k + 1]
        if expression_list[k] in '0123456789' and expression_list[k + 1] in '-+*/':
            expression_list.insert(k + 1, ' ')
        k += 1
        if expression_list[n] in '*/+' and expression_list[n + 1] in '0123456789':
            expression_list.insert(n + 1, ' ')
        n += 1
    expression = ''.join(expression_list)
    return expression


def calc(expression):
    expression = correction(expression)
    while True:
        pattern = r'(\(?-?\d+\.*\d*) [/*+-] (-?\d+\.*\d*\))'
        re_expression = re.finditer(pattern, expression)
        re_exp_list = list(re_expression)
        expression_list = list(expression)
        print(re_exp_list, 'expr_list')

        if re_exp_list != []:
            # print(re_exp_list[0].span())
            a = 0
            s = 0
            x, y = re_exp_list[0].span()
            x, y = int(x) - a + s, int(y) - a + s
            del expression_list[x: y:]
            # print(expression_list, 'del')
            expression_list.insert(x, str(operations_in_brackets(re_exp_list[0][0])))
            # print(expression_list, 'exp')
            expression = ''.join(expression_list)
            s += 1
        else:
            break
    print(expression, 'simpled')
    operations(expression)


def operations_in_brackets(expr):
    # print(expr)
    pattern = r'(-?\d+\.*\d*) ([*/+-])? (-?\d+\.*\d*)\)'
    re_expression = re.findall(pattern, expr)
    # print(list(re_expression))
    # print(re_expression[0], 're[01]')
    a, act, b = re_expression[0]
    # print(a, act, b)
    a = float(a)
    b = float(b)
    if act == '*':
        c = a * b
    elif act == '/':
        c = a / b
    elif act == '+':
        c = a + b
    elif act == '-':
        c = a - b
    # print(c)
    return c


def operations(expression):
    k = 1
    n = ''
    while True:
        r = expression
        # print(expression, k, 'Andriy')
        pattern = r'(-?\d+\.*\d*)\s?([*/])\s?(-?\d+(\.\d)?)'
        re_expression = re.finditer(pattern, expression)
        re_exp_list = list(re_expression)
        expression_list = list(expression)
        # print(re_exp_list, k,  'rrrrr')
        if re_exp_list != []:
            print(re_exp_list, 'es')
            s = 0
            f, d = re_exp_list[0].span()
            x, y = int(f), int(d)
            print(x, y)
            re_split = re_exp_list[0][0].split()
            del expression_list[x: y:]
            print(re_split, 're_split')
            a, act, b = re_split
            # print(a, act, b)
            a = float(a)
            b = float(b)
            if act == '*':
                n = a * b
            elif act == '/':
                n = a / b
            expression_list.insert(x, str(n))
            print([expression], 'e+-', k)
            expression = ''.join(expression_list)
            print(expression, 'joined1')
            k += 1
        else:
            break

    k = 1
    n = ''
    while True:
        r = expression
        # print(expression, k, 'Andriy')
        pattern = r'(-?\d+\.*\d*)\s?([+-])\s?(-?\d+\.*\d*)'
        re_expression = re.finditer(pattern, expression)
        re_exp_list = list(re_expression)
        expression_list = list(expression)
        # print(re_exp_list, k,  'rrrrr')
        if re_exp_list != []:
            print(re_exp_list, 'es')
            s = 0
            f, d = re_exp_list[0].span()
            x, y = int(f), int(d)
            print(x, y)
            re_split = re_exp_list[0][0].split()
            print(re_split, 're_split')
            del expression_list[x: y:]
            a, act, b = re_split
            # print(a, act, b)
            a = float(a)
            b = float(b)
            if act == '-':
                n = a - b
            elif act == '+':
                n = a + b
            expression_list.insert(x, str(n))
            print([expression], 'e+-', k)
            expression = ''.join(expression_list)
            print(expression, 'joined1')
            k += 1
        else:
            break


calc("3 * 1 + ((2 + 3) * (1 + 4) * (2 + 1))")