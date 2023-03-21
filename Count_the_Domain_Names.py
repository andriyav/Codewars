''''
Story

You have a list of domain names from a log file, indicating the number of times the computer accessed those sites. However, the list shows subdomains too, but you want to see only the main sites and the total number of accesses. For example 6.clients-channel.google.com and apis.google.com should be counted together as google.com.
Task

Complete the function that takes two arguments:

    domains is a list of domain names, showing the number of access requests to each domain, as you copied it from the logs
    and the optional min_hits which defines what is the minimum number of accesses in order to appear on the output list. If this is not given, consider it 0.

Return a string ready to be printed, showing the sites with the total number of accesses, in a decreasing order.

Output requirements:

    the output should show the sites with the total number of accesses in parentheses,
    sites should have only 2 levels (e.g. ebay.com), except for .co.xx and .com.xx type domains, which should have 3 levels (e.g. amazon.co.jp),
    the list should be sorted in decreasing order of access,
    if two sites have the same number of accesses, sort them alphabetically,
    entries should be separated by newlines (\n)
'''

import re
def count_domains(domains, min_hits=0):
    reg = re.findall(r'([^.]+(?:\.co|\.com)?\.[^.\s]+)\s+(\d+)', domains)
    unique_list = []
    for unique in reg:
        if unique[0] not in unique_list:
            unique_list.append(unique[0])
    result_list = []
    for unique_ele in unique_list:
        sum = 0
        result_one_list = []
        for sum_element in reg:
            if sum_element[0] == unique_ele:
                sum += int(sum_element[1])
        if sum >= min_hits:
            result_one_list.append(unique_ele)
            result_one_list.append(sum)
        if result_one_list != []:
            result_list.append(result_one_list)
    result_list.sort()
    result_list.sort(reverse=True, key=lambda x: x[1])
    string_result = ''
    for res_ele in result_list:
        string_result += f'\n{res_ele[0]} ({res_ele[1]})'
    result = string_result.strip('\n')
    print(result)
    return result

domains_list = '''
*.amazon.co.uk	89
*.doubleclick.net	139
*.fbcdn.net	212
*.in-addr.arpa	384
*.l.google.com	317
1.client-channel.google.com	110
6.client-channel.google.com	45
a.root-servers.net	1059
apis.google.com	43
clients4.google.com	71
clients6.google.com	81
connect.facebook.net	68
edge-mqtt.facebook.com	56
graph.facebook.com	150
mail.google.com	128
mqtt-mini.facebook.com	47
ssl.google-analytics.com	398
star-mini.c10r.facebook.com	46
staticxx.facebook.com	48
www.facebook.com	178
www.google.com	162
www.google-analytics.com	127
www.googleapis.com	87'''
count_domains(domains_list, 0)