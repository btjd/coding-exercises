"""
LeetCode 681
Given a time represented in the format "HH:MM", form the next closest time 
by reusing the current digits. There is no limit on how many times a digit 
can be reused.

You may assume the given input string is always valid. For example, "01:34", 
"12:09" are all valid. "1:34", "12:9" are all invalid.

Algorithm: We first scan a rotated minutes array starting
           from current minutes + 1 and ending at the same start time.
           when we find minutes whose digits we can use, we set
           that to be our new minutes, if it's smaller than our initial
           minutes, it means we had to go past the 60 minute mark and a
           new hour needs to be calculated using the same method.
"""

def next_closest_time(time):
    digits = set(map(int, ''.join(time.split(':'))))
    hours, minutes = time.split(':')
    int_hours = int(hours)
    int_minutes = int(minutes)
    
    calc_new_hours = False
    
    out_minutes = ""
    out_hours = ""
    
    for m in range(int_minutes + 1, 60) + range(0, int_minutes + 1):
        if m//10 in digits and m%10 in digits:
            out_minutes = m
            if m <= int_minutes:
                calc_new_hours = True
            break
    
    if calc_new_hours:
        for h in range(int_hours + 1, 24) + range(0, int_hours + 1):
            if h//10 in digits and h%10 in digits:
                out_hours = h
                break
                
        return str(out_hours//10)+str(out_hours%10)+":"+str(out_minutes//10)+str(out_minutes%10)
    
    else:
        return hours+":"+str(out_minutes//10)+str(out_minutes%10)
def test_next_closest_time():
    assert next_closest_time("22:37") == "23:22"
    assert next_closest_time("00:00") == "00:00"
    assert next_closest_time("01:59") == "05:00"
    assert next_closest_time("19:34") == "19:39"
    assert next_closest_time("23:59") == "22:22"
    