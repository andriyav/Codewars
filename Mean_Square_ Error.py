def solution(array_a, array_b):
    dif = 0
    for i in range(0, len(array_a)):
        dif += (abs(array_a[i] - array_b[i]))**2
    return dif/len(array_a)




solution([-1, 0], [0, -1])
