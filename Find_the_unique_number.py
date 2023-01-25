'''https://www.codewars.com/kata/585d7d5adb20cf33cb000235/python'''
def find_uniq(arr):
    counter = {}  
    for number in arr:
        counter[number] = counter.get(number, 0) + 1
    for key, value in counter.items():
        if value == 1:
            return key






find_uniq([0, 0, 0.55, 0, 0])