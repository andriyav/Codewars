from cmath import exp
import re


def calc(expression):
    while True:
        pattern = r'(-?\d+.?\d? [/*+-] -?\d+.?\d?)'
        re_expression = re.finditer(pattern, expression)
        re_exp_list = list(re_expression)
        expression_list = list(expression)
        print(re_expression)
        if re_exp_list != []:
            print(re_exp_list[0].span())
            a = 0
            s = 0
            x, y = re_exp_list[0].span()
            x, y = int(x) - a + s, int(y) - a + s
            del expression_list[x: y:]
            print(expression_list, 'del')
            expression_list.insert(x, str(operations_in_brackets(re_exp_list[0][0])))
            print(expression_list, 'exp')
            expression = ''.join(expression_list)

            s += 1
        else:
            break
    print(expression, 'simpled')
    # operations(expression)


def operations_in_brackets(expr):
    print(expr)
    pattern = r'(-?\d+.?\d?) ([*/+-]) (-?\d+.?\d?)'
    re_expression = re.findall(pattern, expr)
    print(re_expression[0], 're[01]')
    a, act, b = re_expression[0]
    print(a, act, b)
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
    print(c)
    return c




def operations(expr):
    pattern = r'(-?\d+) ([*/]) (-?\d+)'
    re_expression = re.findall(pattern, expr)
    print(re_expression[0])
    a, act, b = re_expression[0]
    print(a, act, b)
    a = float(a)
    b = float(b)
    if act == '*':
        c = a * b
    elif act == '/':
        c = a / b
    print(c)

calc("-7 + (-7 - -33) - (3 + 4)")