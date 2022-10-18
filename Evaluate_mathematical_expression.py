import re
def calc(expression):
    pattern = r'(\(\d+ [/*+-] \d+\))'
    re_expression = re.finditer(pattern, expression)
    for i in re_expression:
        print(i.span())
    list_expres = list(expression)
    print(list_expres[7])
    # math_re_expression = list(map(eval, re_expression))
    print(eval("-7 * -((64 * 3) -3 + 4 + (4 + 4))"))











calc("-7 * -((64 * 3) -3 + 4 + (4 + 4))")