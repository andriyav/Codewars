def sum_of_intervals(intervals):
    while len(intervals) > 1:
        a = intervals[0]
        b = intervals[1]
        overlap = max(0, min(a[1], b[1]) - max(a[0], b[0]))
        total_len = (a[1]-a[0]) + (b[1]-b[0])
        new_intervals = [[min(a[0], b[0]), max(a[1], b[1])]]
        intervals = new_intervals.copy()
    print(max(a[1], b[1]))
    print(min(a[0], b[0]))
    print(total_len, 'total_len')
    print(overlap, 'overlap')
    print(new_intervals, 'new_intervals')
    print(intervals, 'intervals')
sum_of_intervals([
[1, 4],
[3, 5],
[7, 10]
])
