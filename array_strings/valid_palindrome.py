"""
LeetCode 125
Given a string, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty 
string as valid palindrome.
"""

def is_palindrome(s):
    start = 0
    end = len(s)-1
    while start < end:
        while not s[start].isalnum() and start < end:
            start += 1
        while not s[end].isalnum() and start < end:
            end -= 1
        if s[start].lower() == s[end].lower():
            start += 1
            end -= 1
        else:
            return False
    return True

def test_is_palindrome():
    assert is_palindrome(".,") is True
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False