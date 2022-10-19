from cmath import exp
import re


def calc(expression):
    pattern = r'(\(\d+ [/*+-] \d+\))'
    re_expression = re.finditer(pattern, expression)
    expression_list = list(expression)
    a = 0
    s = 0
    for i in re_expression:
        print(i.span())
        x, y = i.span()
        x, y = int(x) - a + s, int(y) - a + s
        del expression_list[x: y:]
        # expression_list.insert(x + a, str(operations(i[0])))
        a = y - x
        print(expression_list, 'exp')
        expression_list_simpled = ''.join(expression_list)
        print(expression_list_simpled)
        s += 1


def operations(expr):
    pattern = r'(\d+) *([*/+-]) *(\d+)+'
    re_expression = re.findall(pattern, expr)
    print(re_expression[0])
    a, act, b = re_expression[0]
    print(a, act, b)
    a = int(a)
    b = int(b)
    if act == '*':
        c = a * b
    elif act == '/':
        c = a / b
    elif act == '+':
        c = a + b
    elif act == '-':
        c == a - b
    print(c)
    return c


calc("-7 * -((64 *3) -3 + 4 + (4 + 4)) ")

# operations(('64', '*', '3'))