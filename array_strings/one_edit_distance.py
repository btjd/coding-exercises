"""
LeetCode 161
Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t

Algorithm/approach:
We are essentially dealing with two distinct cases:
1- Both strings have the same length, where then we
   can use the same pointer to traverse both strings
   and we can find at most, a difference of one car.
   Note that the diff cannot be 0 either because in
   that case, both input strings are identical
2- The input strings have different lengths. We
   traverse them with different pointers and keep 
   track of the diff which again, cannot be more than
   1. When we find a diff, the pointer of the shorter
   string stays in place while the pointer of the longer
   string advances by 1. This can only happen once. in
   the end if the diff is no more than 1, we are good.
"""

def one_edit_distance(s, t):
    def longer_shorter(longer, shorter):
        i=0
        j=0
        diff=0
        while i<len(longer) and j<len(shorter) and diff<=1:
            if longer[i]!=shorter[j]:
                i+=1
                diff+=1
            else:
                i+=1
                j+=1
        if diff<=1:
            return True
        else:
            return False
    if (len(s)==0 and len(t)==1) or (len(s)==1 and len(t)==0):
        return True
    elif abs(len(s)-len(t))>1:
        return False
    elif s=="" or t=="":
        return False
    elif len(s)==len(t):
        i=0
        diff=0
        while i<len(s) and diff<=1:
            if s[i]==t[i]:
                i+=1
            else:
                diff+=1
                i+=1
        if diff==1:
            return True
        else:
            return False
    else:
        if len(s)>len(t):
            return longer_shorter(s, t)
        else:
            return longer_shorter(t, s)

def test_one_edit_distance():
    assert one_edit_distance('cab', 'ad') is False
    assert one_edit_distance('a', 'a') is False
    assert one_edit_distance('a', 'c') is True
    assert one_edit_distance('', '') is False
    assert one_edit_distance('a', '') is True # Line 45
    assert one_edit_distance('', 'a') is True # Line 45
    assert one_edit_distance('ab', 'acb') is True
    assert one_edit_distance('1203', '1213') is True