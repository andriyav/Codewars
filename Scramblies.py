def scramble(s1, s2):
    for i in s2:
        if i in s1:
            continue
        else:
            print('False')
            return False
    print('True')
    return True
scramble("pgzwvlpcbshrbavy", "svghbvbpwywl")
