"""Your task is to remove all consecutive duplicate words from a string, leaving only first words entries."""
def remove_consecutive_duplicates(s):
    s_splite = s.split(' ')
    if len(s_splite) == 1:
        return s
    result = []
    n = 0
    while n + 1 < len(s_splite):
        if s_splite[n] != s_splite[n+1]:
            result.append(s_splite[n]) 
        n += 1
    split_last = s_splite[-1:]
    result.append(split_last[0])
    result = ' '.join(result)
    return result



remove_consecutive_duplicates("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta")