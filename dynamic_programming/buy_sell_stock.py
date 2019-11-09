"""
Leetcode 121
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell 
one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Algorithm:
current profit = current price - recorded min price
with every iteration we compare keep track and update min
price if we find a smaller value. Then we immediately
compare our current max profit to (current price - min 
recorded price)
"""
def buy_sell_stock(prices):
    max_profit = 0
    min_price = float('inf')
    for e in prices:
        # As we iterate through the list, we keep track
        # of the smallest price we encouter so we can use
        # it as our buy stock
        min_price = min(e, min_price)
        # max profit is max of current max profit and
        # current price minus min recorded price
        max_profit = max(max_profit, e - min_price)
    return max_profit

def test_buy_sell_stock():
    assert buy_sell_stock([7,1,5,3,6,4]) == 5
    assert buy_sell_stock([7,6,4,3,1]) == 0