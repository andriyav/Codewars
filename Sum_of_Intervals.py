def sum_of_intervals(intervals):
    total_len = 0
    while len(intervals) >= 2:
        a = intervals[0]
        b = intervals[1]
        overlap = max(0, min(a[1], b[1]) - max(a[0], b[0]))
        two_len = (a[1]-a[0]) + (b[1]-b[0])
        total_len += two_len
        total_len -= overlap

        print(total_len, intervals)
        print(total_len, 'total_len')
        print(overlap, 'overlap')
        intervals.pop(0)
        intervals.pop(0)
        print(total_len, intervals)
    if len(intervals) == 1:
        total_len += (intervals[0][1]-intervals[0][0])
    print(total_len, 'total_len')


        # new_intervals = [[min(a[0], b[0]), max(a[1], b[1])]]

        # length = len(intervals)
        # print(length, 'length', intervals[-length+2:])
        # last_of_int = intervals[-length+2:]
        # print(last_of_int[0])
        # for i in last_of_int:
        #
        #     new_intervals.append(i)
        #     print(new_intervals)
        #     intervals = new_intervals.copy()
        #     print(intervals, 'intervals')

    # print(max(a[1], b[1]))
    # print(min(a[0], b[0]))
    # print(total_len, 'total_len')
    # print(overlap, 'overlap')
    # print(new_intervals, 'new_intervals')
    # print(intervals, 'intervals')
sum_of_intervals([
[1, 3],
[4, 5],
[5, 10],
[4, 12],
[12, 13]
]
)
