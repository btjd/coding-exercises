"""
LeetCode 394
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string 
inside the square brackets is being repeated exactly k times. 
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, 
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits 
and that digits are only for those repeat numbers, k. For example, there won't 
be input like 3a or 2[4].

Algorithm:
https://leetcode.com/problems/decode-string/discuss/87662/Python-solution-using-stack
Scan the string linerarly, and as you find digits and letters, build them in 
the variables count and res. Everytime we find a [, we push res and count to a
stack and reset them. When we run into ] we pop the last pair of count and res
and we update the overall solution to be: string_from_stack + (count_from_stack + current_res)
For example, in the case of 3[a], that becomes ''+(3*'a'). That means, 3[a]2[bc] is
'aaa'+(2*'bc')
"""

def decode_string(s):
    res = ''
    count = 0
    stack = []
    for c in s:
        if c.isdigit():
            count = (count * 10) + int(c)
        elif c.isalpha():
            res += c
        elif c == '[':
            stack.append(res)
            stack.append(count)
            res = ''
            count = 0
        elif c == ']':
            n = stack.pop()
            prev = stack.pop()
            res = prev + (n*res)
    return res

def test_decode_string():
    assert decode_string("3[a]2[bc]") == "aaabcbc"
    assert decode_string("3[a2[c]]") == "accaccacc"
    assert decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef"