""""
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future 
to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

"""

# solution 1. fails in long strings because is O(n^2) complexity
def max_profit(prices: list[int])-> int :
    max_pro = 0
    for i in range(len(prices) -1) :
        for j in range(i +1, len(prices)) :
            max_pro = max(max_pro, prices[j] - prices[i])
    return max_pro

# solution 2. It has O(n) complexity
def max_profit_II(prices: list[int])-> int:
    profit = 0
    bp = prices [0] # bp = buy price
    for price in prices[1:]:   # loop since index 1 because index 0 is aready readen
        if price < bp:
            bp = price
            continue
        profit = max(profit, price - bp)

    return profit

a = [7, 1, 5, 3, 6, 4]


print(max_profit(a))
print(max_profit_II(a))