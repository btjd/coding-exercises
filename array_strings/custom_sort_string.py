"""
LetCode 791
S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so 
that they match the order that S was sorted. More specifically, if x occurs before y in S, 
then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.
"""
import collections

def custom_srot_string(S, T):
    # count[char] will be the number of occurrences of
    # 'char' in T.
    count = collections.Counter(T)
    ans = []

    # Write all characters that occur in S, in the order of S.
    for c in S:
        ans.append(c * count[c])
        # Set count[c] = 0 to denote that we do not need
        # to write 'c' to our answer anymore.
        count[c] = 0

    # Write all remaining characters that don't occur in S.
    # That information is specified by 'count'.
    for c in count:
        ans.append(c * count[c])

    return "".join(ans)

def custom_srot_string_2(S, T):
    ans = []
    for i in S:
            ans.append(i*T.count(i))
    for i in T:
        if i not in S:
            ans.append(i)
    return ''.join(ans)

def test_custom_srot_string():
    assert custom_srot_string("cba", "abcd") == "cbad"
    assert custom_srot_string("kqep", "pekeq") == "kqeep"
    assert custom_srot_string("cbafg", "abcd") == "cbad"