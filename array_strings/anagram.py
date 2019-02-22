def anagram(alist1, alist2):
    buff = {}
    for c in alist1:
        if c not in buff:
            buff[c] = 1
        else:
            buff[c] += 1
    for c in alist2:
        if c not in buff:
            buff[c] = 1
        else:
            buff[c] += 1
    for k in buff:
        if buff[k] % 2 != 0:
            return False
    return True

alist1 = 'baabaa'
alist2 = 'abaaba'
print(anagram(alist1, alist2))