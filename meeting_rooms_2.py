"""
Given an array of meeting time intervals consisting of 
start and end times [[s1,e1],[s2,e2],...] (si < ei), 
find the minimum number of conference rooms required.
"""
def min_meeting_rooms(intervals):
    if intervals == []:
        return 0
    elif len(intervals) == 1:
        return 1
    else:
        intervals.sort()
        print(intervals)
        conf_rooms = 1
        max_end = intervals[0][1]
        for i in range(1, len(intervals) - 1):
            current_start = intervals[i][0]
            current_end = intervals[i][1]
            previous_end = intervals[i-1][1]
            if current_end <= max_end:
                if current_start >= previous_end:
                    continue
                else:
                    conf_rooms += 1
            else:
                max_end = current_end
                if current_end >= previous_end:
                    continue
                else:
                    conf_rooms += 1
    return conf_rooms


print(min_meeting_rooms([[6,10],[2,4],[3,13],[0,7],[9,11]]))