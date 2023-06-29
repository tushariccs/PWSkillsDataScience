<<<<<<< HEAD
def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False

    return True
intervals = [[0, 30], [5, 10], [15, 20]]
=======
def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False

    return True
intervals = [[0, 30], [5, 10], [15, 20]]
>>>>>>> 7caea318e86370ce5b856e0aaf2784353e6ad797
print(canAttendMeetings(intervals))  # Output: False