def sum_of_intervals(intervals):
    result = 0
    new_intervals = []
    intervalss = intervals.copy()
    non_overlap_list = []
    overlap_list = []
    result_list = []
    unique = []
    n = 0
    k = 0
    while len(intervals) > n:

        while len(intervals) > k + 1:

            a = intervals[k]
            b = intervals[n]
            if a != b:
                overlap = max(0, min(a[1], b[1]) - max(a[0], b[0]))
                if overlap > 0:
                    new_intervals = [min(a[0], b[0]), max(a[1], b[1])]
                    intervals.append(new_intervals)
                    overlap_list.append(new_intervals)
                    intervals.pop(0)
                    intervals.pop(0)
                else:
                    non_overlap_list.append(b)
                    non_overlap_list.append(a)
                    intervals.append(a)
                    intervals.append(b)
                    intervals.pop(0)
                    intervals.pop(0)
            k += 1
        n += 1
    print(intervals, 'intervals')
    print(non_overlap_list, 'non_overlap_list')
    for m in non_overlap_list:
        a = intervals[0]
        b = m
        overlap = max(0, min(a[1], b[1]) - max(a[0], b[0]))
        new_intervals = [min(a[0], b[0]), max(a[1], b[1])]
        if overlap > 0:
            intervals.append(new_intervals)
            result_list.append(new_intervals)
        else:
            result_list.append(m)

        result_list.append(intervals[0])
    for i in result_list:
        if i not in unique:
            unique.append(i)
    print(unique)


sum_of_intervals([
    [1, 5],
    [10, 20],
    [1, 6],
    [16, 19],
    [5, 11]