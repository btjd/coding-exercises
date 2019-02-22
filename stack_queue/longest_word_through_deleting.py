"""
LeetCode 524
Given a string and a string dictionary, find the longest string 
in the dictionary that can be formed by deleting some characters 
of the given string. If there are more than one possible results, 
return the longest word with the smallest lexicographical order. 
If there is no possible result, return the empty string.
"""

def longest_word(s, d):
    if s == "" or not d:
        return ""
    else:
        res = []
        # This is to find out if we have multiple
        # results with the same word length, in
        # which case we need to the longest word
        # with the smallest lexicographical order
        count = set()
        for word in d:
            # We load our dictionary word
            # into a queue
            q = list(word)
            # We record the size of the word
            # this will help us retrieve the 
            # longest result
            wl = len(word)
            # We loop through each char of s
            # and deque every time we find a 
            # match
            for c in s:
                if q and q[0] == c:
                    q.pop(0)
            # If after we finish going through the string
            # the queue is empty, we found a word
            # that matched.
            if not q:
                res.append((word, wl))
                count.add(wl)
        # First we check if we obtained any results,
        # then for either cases, we want to sort so
        # results are ordered in lecxicographical order.
        # In cased we get many results of the
        # same length, we want to just return the first item.
        if res:
            res.sort()
            if len(count) == 1:
                return res[0][0]
            # If we get multiple results, including when the
            # max subset has multiple entries, we filter out
            # the max entries get the first item.
            else:
                filtered_res = [x for x in res if x[1] == max(count)]
                return filtered_res[0][0]
        else:
            return ""

def test_longest_word():
    assert longest_word("abpcplea", ["ale","apple","monkey","plea"]) == "apple"
    assert longest_word('abpcplea', ["a","b","c"]) == "a"
    assert longest_word("bab", ["ba","ab","a","b"]) == "ab"