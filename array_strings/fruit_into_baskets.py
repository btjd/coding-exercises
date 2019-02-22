"""
LeetCode 904
In a row of trees, the i-th tree produces fruit with type tree[i].
You start at any tree of your choice, then repeatedly perform the following steps:

1) Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
2) Move to the next tree to the right of the current tree.  
   If there is no tree to the right, stop.

Note that you do not have any choice after the initial choice of starting tree: 
you must perform step 1, then step 2, then back to step 1, then step 2, and so on 
until you stop.
You have two baskets, and each basket can carry any quantity of fruit, 
but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?
"""
def total_fruit(tree):
    """
    :type tree: List[int]
    :rtype: int
    """
    if not tree:
        return 0
    bucket1 = None
    bucket2 = None
    fruit_count_list = []
    fruit_count = 0
    i = 0
    # Start of new sliding window
    reset_index = 0
    while i < len(tree):
        """
        Start of a window, two empty buckets,
        go ahead and put your first fruit in 
        bucket1, increment fruit count.
        """
        if bucket1 == None and bucket2 == None:
            bucket1 = tree[i]
            fruit_count += 1
            i += 1
        # """
        # If we are here, bucket1 already has something
        # in it and bucket 2 is still empty. If it's
        # a different kind of fruit from what we have
        # in bucket1, go ahead and put it in bucket2,
        # then increment fruit count. This is also where
        # a new sliding window would start if we encouner
        # a third kind of fruit.
        # """
        elif bucket2 == None and tree[i] != bucket1:
            bucket2 = tree[i]
            fruit_count += 1
            reset_index = i
            i += 1
        # """
        # If we are here, both bucke1 and bucket2 have
        # fruit in them and we are still running into
        # trees that have fruit that is in either bucket
        # """
        elif tree[i] == bucket1 or tree[i] == bucket2:
            fruit_count += 1
            i += 1
        # """
        # If we are here, our conditions have been broken
        # and we need to update our fruit count list with
        # this current count, reset fruit count to be used
        # in a new window that we are going to start by 
        # setting i to the reset index previously recorded
        # in line 38.
        # """
        else:
            fruit_count_list.append(fruit_count)
            fruit_count = 0
            bucket1 = None
            bucket2 = None  
            i = reset_index
    # """
    # If we are here, we have just completed our last
    # window and didn't get to update our fruit count
    # list within the loop, so we do it here. We then
    # finally return the max value of all the recorded
    # fruit counts.
    # """
    fruit_count_list.append(fruit_count)
    return max(fruit_count_list)

def test_fruit_basket():
    assert total_fruit([1,2,1]) == 3
    assert total_fruit([0,1,2,2]) == 3
    assert total_fruit([1,2,3,2,2]) == 4
    assert total_fruit([3,3,3,1,2,1,1,2,3,3,4]) == 5