'''You have a positive number n consisting of digits. You can do at most one operation: Choosing the index of a digit in the number, remove this digit at that index and insert it back to another or at the same place in the number in order to find the smallest number you can get.
Task:

Return an array or a tuple or a string depending on the language (see "Sample Tests") with

        the smallest number you got
        the index i of the digit d you took, i as small as possible
        the index j (as small as possible) where you insert this digit d to have the smallest number.
'''
def smallest(n):
    n_str_list = list(str(n)) #  перевід в ліст стрічками
    n_int_list = list(map(int, n_str_list)) #  перевід ліст в інтеджер
    n_int_list_muteable = n_int_list.copy()
    range_len = len(n_int_list)
    min_list = n_int_list_muteable.copy()
    result6 = []
    #  переміщенні кожної цифри з ліва на право
    for g1 in range(0, range_len): 
        n_int_list_muteable = n_int_list.copy()
        for g2 in range(2, range_len+1):         
            n_int_list_muteable.insert(g2+g1, n_int_list[g1])
            n_int_list_muteable.pop(g2+g1-2)
            if int(''.join(list(map(str, n_int_list_muteable)))) < int(''.join(list(map(str, min_list)))): # зі всього переліку залишається найменше число
                min_list = n_int_list_muteable.copy()
                result6 = [g1, g2-1]
            if g1 + g2 >= range_len:
                break
    indexes = int(''.join(list(map(str, min_list))))
    result6.insert(0, indexes)
    range_len = len(n_int_list)
    min_list = n_int_list_muteable.copy()
    #  переміщенні кожної цифри з права на ліво
    result7 = []
    g = 0
    for g1 in range(range_len, -1, -1):
        n_int_list_muteable = n_int_list.copy()
        for g2 in range(range_len, 1+g, -1):
            n_int_list_muteable.insert(g2-2-g, n_int_list[g1-1])
            n_int_list_muteable.pop(g2-g)
            if int(''.join(list(map(str, n_int_list_muteable)))) <= int(''.join(list(map(str, min_list)))):
                min_list = n_int_list_muteable.copy()
                result7 = [g1-1, g2-2-g]              
        g += 1
    indexes = int(''.join(list(map(str, min_list))))
    result7.insert(0, indexes)
    a = [result6, result7]
    a = sorted(a, key=lambda a_entry: a_entry[0]) #  сортування за найменшим першого згаченгя списку з індексами двох методів для виділення найменшого
    result = a[0] #  виділеня першого найменшого значення
    return result

smallest(199819884756)