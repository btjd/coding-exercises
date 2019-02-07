def license_key_formatting(S, K):
    Slist = list(S)
    i = 0
    while i < len(Slist):
        if Slist[i].isalpha():
            Slist[i] = Slist[i].upper()
            i += 1
        elif Slist[i] == '-':
            Slist.pop(i)
        else:
            i += 1
            
    j = len(Slist)-K
    while j > 0:
        Slist.insert(j, '-')
        j = j-K
    return ''.join(Slist)

def test_license_key_formatting():
    assert (license_key_formatting("5F3Z-2e-9-w", 4)) == "5F3Z-2E9W"
    assert (license_key_formatting("2-5g-3-J", 2)) == "2-5G-3J"