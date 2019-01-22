def list_sum(arr):
    """
    :param arr:
    :return: Given a list [1, 1], increment its value by 1 so it becomes [1, 2]
             In case of [9, 9] as an input, output should be [1, 0, 0]
    """
    i = len(arr) - 1
    return _rec_list_sum(arr, i)

def _rec_list_sum(arr, i):
    if i == 0 and arr[i] == 9:
        arr[i] = 1
        arr.insert(1, 0)
        return arr
    elif i > 0 and arr[i] == 9:
        arr[i] = 0
        return _rec_list_sum(arr, i - 1)
    elif i >= 0 and arr[i] < 9:
        arr[i] += 1
        return arr
    # elif i == 0 and arr[i] < 9:
    #     arr[i] += 1
    #     return arr


def incremet_iter(arr):
    carry = 0
    last = len(arr) - 1
    for i in range(last, -1, -1):
        if i == last and arr[i] == 9:
            arr[i] = 0
            carry = 1
        elif i == last and arr[i] != 9:
            arr[i] += 1
        elif i > 0 and carry == 1:
            if arr[i] != 9:
                arr[i] += 1
                carry = 0
            else:
                arr[i] = 0
                carry = 1
        elif i == 0 and carry == 1:
            if arr[i] == 9:
                arr[i] = 0
                arr.insert(0, 1)
            else:
                arr[i] += 1
    return arr


arr = [1, 3, 5]
res = list_sum(arr)
print res