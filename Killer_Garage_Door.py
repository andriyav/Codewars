def controller(events):
    result = []
    result_total = ''
    m = 0
    buton = 1
    direction = 1 
    for i in events:
        if i == 'P':
            buton *= -1
        if i == 'O':
            direction *= -1    
        if buton == 1:
            n = str(m)
            result.append(n)
        if buton == -1 and direction == 1:
            if m < 5:
                m += 1
            n = str(m)
            if m == 5:
                direction *= -1
                buton = 1
            result.append(n)         
        if buton == -1 and direction == -1:
            if m > 0:
                m -= 1
            n = str(m)
            if m == 0:
                direction *= -1
                buton = 1
            result.append(n)      
        result_total = ''.join(result)
    print(result_total)


           
controller('..PO..P..P..P..P.OOO....P..........P..O..P.O.P.OP.P.P....P.PPP..PP.......P....PP..PP..P.O.......PO.P')