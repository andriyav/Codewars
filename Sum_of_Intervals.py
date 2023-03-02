def sum_of_intervals(intervals):
    new_intervals = []
    cycle = 10
    result = 0
    unique = []
    while cycle > 1:
        for a in intervals:
            for b in intervals:
                if a != b:
                    overlap = max(0, min(a[1], b[1]) - max(a[0], b[0])) # число перекриття двох інтервалів
                    if overlap > 0:
                        new_intervals = [min(a[0], b[0]), max(a[1], b[1])] # заміна двох інтервалів занальним
                        intervals.insert(0, new_intervals) # додавання нового інтервалу на початок листа
                        intervals.pop(intervals.index(a)) # видалення двох злитів інтервалів
                        intervals.pop(intervals.index(b))
                        break
        cycle -= 1
    for u in intervals: # видалення однакових інтервалів
        if u not in unique:
            unique.append(u)
    for s in unique: # розрахунок довжини інтервалів
        item_len = s[1] - s [0]
        result += item_len
    print(result)
sum_of_intervals([[1, 5], [1, 5], [30, 34], [35, 37], [35, 38], [2, 3], [4, 8]])