'''Given a string and an array of integers representing indices, capitalize all letters at the given indices.

For example:

    capitalize("abcdef",[1,2,5]) = "aBCdeF"
    capitalize("abcdef",[1,2,5,100]) = "aBCdeF". There is no index 100.

The input will be a lowercase string with no spaces and an array of digits.'''

def capitalize(s, ind):
    result = []
    for index in range(len(s)):
        if index in ind:
            result.append(s[index].upper())
        else:
            result.append(s[index])
    result = ''.join(result)
    return result


    print(''.join(s[index].upper() if index in ind else s[index] for index in range(len(s))))


capitalize("abracadabra",[2,6,9,10])