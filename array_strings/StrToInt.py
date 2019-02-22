def atoi(input_str):
    ret = 0
    for s in range(len(input_str)):
        ret = ret*10 + (ord(input_str[s]) - ord('0'))
    return ret
