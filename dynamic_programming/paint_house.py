"""
Leetcode 256
There are a row of n houses, each house can be painted with 
one of the three colors: red, blue or green. The cost of 
painting each house with a certain color is different. 
You have to paint all the houses such that no two adjacent 
houses have the same color.

The cost of painting each house with a certain color is 
represented by a n x 3 cost matrix. For example, costs[0][0] 
is the cost of painting house 0 with color red; costs[1][2] 
is the cost of painting house 1 with color green, and so on... 
Find the minimum cost to paint all houses.

Algorithm:
Start with house 1, then traverse the rest of the houses. In
each iteration, for every color, the cumulative cost is the
current cost plust the min of the other two colors from the 
previous house. In the end we just need to look at the last
house and and get the min value from it.
https://youtu.be/fZIsEPhSBgM?t=93
"""

def min_cost(costs):
    if not costs:
        return 0
    else:
        for i in range(1, len(costs)):
            costs[i][0] += min(costs[i-1][1], costs[i-1][2])
            costs[i][1] += min(costs[i-1][0], costs[i-1][2])
            costs[i][2] += min(costs[i-1][0], costs[i-1][1])
    last = len(costs)-1
    return min(min(costs[last][0], costs[last][1]), costs[last][2])

def test_min_cost():
    assert min_cost([[17,2,17],[16,16,5],[14,3,19]]) == 10
    assert min_cost([[3,5,3],[6,17,6],[7,13,18],[9,10,18]]) == 26
    assert min_cost([[5,8,6],[19,14,13],[7,5,12],[14,15,17],[3,20,10]]) == 43