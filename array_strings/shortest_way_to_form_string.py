def shortest_form_string(source, target):
    source_set = set(source)
    substr = ''
    s = 0
    t = 0
    count = 0
    while t < len(target):
        if target[t] not in source_set:
            return - 1
        while s < len(source) and t < len(target):
            if source[s] == target[t]:
                substr += source[s]
                s += 1
                t += 1
            else:
                s += 1
        count += 1
        substr = ''
        s = 0
    return count

def test_shortest_form_string():
    assert shortest_form_string('abc', 'abcbc') == 2
    assert shortest_form_string('xyz', 'xzyxz') == 3
    assert shortest_form_string('xyz', 'zyxzyxyz') == 5
    assert shortest_form_string('abc', 'acdbc') == -1
    assert shortest_form_string('aaaaa', 'aaaaaaaaaaaaa') == 3
