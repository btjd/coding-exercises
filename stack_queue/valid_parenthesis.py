"""
LeetCode 20
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
"""

def valid_parenthesis(s):
    """
    :type s: str
    :rtype: bool
    """
    lookup = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    stack = []
    for b in s:
        if b in lookup.values():
            stack.append(b)
        elif b in lookup.keys() and stack == []:
            return False
        elif b in lookup.keys():
            if lookup[b] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            return False
    return stack == []

def test_valid_parenthesis():
    assert valid_parenthesis("()") is True
    assert valid_parenthesis("()[]{}") is True
    assert valid_parenthesis("(]") is False
    assert valid_parenthesis("([)]") is False
    assert valid_parenthesis("{[]}") is True