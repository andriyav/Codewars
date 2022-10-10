'''Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

    Only lower case letters will be used (a-z). No punctuation or digits will be included.
    Performance needs to be considered.
'''
import string
def scramble(s1, s2):
    s1_list = list(s1)
    s2_list = list(s2)
    for i in list(string.ascii_lowercase):
        n1 = s1_list.count(i)
        n2 = s2_list.count(i)
        if n1 >= n2:
            continue
        else:
            return False
    return True


scramble("acgyfgumwea", "awcmuayyf")
