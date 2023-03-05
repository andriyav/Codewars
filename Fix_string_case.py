'''In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:

    make as few changes as possible. If the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
'''

def solve(s):
    return s.lower() if len([i for i in s if i.islower()]) >= len([i for i in s if i.isupper()]) else s.upper()
solve("ACOee")