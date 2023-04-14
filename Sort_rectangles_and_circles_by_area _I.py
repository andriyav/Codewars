''' In this kata you will be given a sequence of the dimensions of rectangles ( sequence with width and length ) and circles ( radius - just a number ).
Your task is to return a new sequence of dimensions, sorted ascending by area.'''


def sort_by_area(seq):
    return sorted(seq, key=lambda x: x[0] * x[1] if isinstance(x, tuple) else 3.14 * x ** 2)


sort_by_area([(1.342, 3.212), (10, 10), 200, (4.23, 6.43)])
