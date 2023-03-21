'''Here, there are 4 different substrings: 721, 245, 111111, and 9. The sums of their digits are 10, 11, 6, and 9 respectively. Therefore, the substring with the largest sum of its digits is 245, and its sum is 11.

Write a function largest_sum which takes a string and returns the maximum of the sums of the substrings. In the example above, your function should return 11.'''

def largest_sum(s):
    # split_s = s.split('0')
    # result = []
    # for string in split_s:
    #     sum = 0
    #     for num in string:
    #         sum += int(num)
    #     result.append(sum)
    # max_s = split_s[result.index(max(result))]
    # sum_res = 0
    # for num_r in max_s:
    #     sum_res += int(num_r)
    # return sum_res
 
    return max(sum(map(int, x)) for x in s.split("0"))
    
    pass # Your code here


largest_sum("72102450111111090")