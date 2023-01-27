"""https://www.codewars.com/kata/633b8be2b5203f003011d79e/python"""
from collections import Counter
def freq_stack(pops, balloons):
    result = []
    while True:
        counter_dict = Counter(balloons)
        max_element_count = max(counter_dict, key=lambda key: counter_dict[key])
        max_count = counter_dict[max_element_count]
        elemts_max_counts = list(filter(lambda elem: elem[1] == max_count, counter_dict.items()))
        indexes_max_counts_list = []
        for i in elemts_max_counts:
            indexes_max_counts = len(balloons) - balloons[::-1].index(i[0]) - 1
            indexes_max_counts_list.append(indexes_max_counts)
        max_indexes_max_counts = max(indexes_max_counts_list)
        pop_element = balloons.pop(max_indexes_max_counts)
        result.append(pop_element)
        pops -= 1
        if pops <= 0:
            break
    print(result)
    return result

freq_stack(4, [5, 7, 5, 7, 4, 5])