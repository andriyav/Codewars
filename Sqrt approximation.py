'''https://www.codewars.com/kata/52ecde1244751a799b00018a/solutions/python'''

def sqrt_approximation(number):
    n = 2
    k = (len(str(number)) * 3) + 1 
    while True:
        number_d = number/n
        n = (number_d + n)/2
        k -= 1
        if k <= 0:
            break
    if abs(round(number_d) - number_d) < 0.0001:
        return round(number_d)
    else:
        return [round(number // number_d), (number // number_d) + 1]