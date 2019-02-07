"""
LeetCode 890
"""
def find_replace_pattern(words, pattern):
    # Helper function that decontructs a
    # word to a discernable pattern by mapping
    # every letter to the list of indexes it
    # appears in. for example, "abb" would 
    # return {"a": [0], "b":[1,2]}
    def _helper(w):
        pattern_d = {}
        for i, c in enumerate(w):
            if c not in pattern_d:
                pattern_d[c] = [i]
            else:
                pattern_d[c].append(i)
        return pattern_d
    
    res = []
    patt = _helper(pattern)
    
    # Once we have a mappig of letters to
    # indices in a string, we just need to
    # compare the sorted list of dictionary
    # values, if they are the same, it's a match
    for word in words:
        pattern = _helper(word)
        if sorted(patt.values()) == sorted(pattern.values()):
            res.append(word)
    return res

def test_find_replace_pattern():
    assert find_replace_pattern(["abc","deq","mee","aqq","dkd","ccc"], "abb") == ["mee","aqq"]
    assert find_replace_pattern(["abc","deq","mee","aqq","dkd","ccc"], "aab") == []