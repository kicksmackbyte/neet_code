'''

# Prompt

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.


# Constraints

1 <= prices.length <= 105
0 <= prices[i] <= 104


'''

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        minimum_purchase = prices[0]

        for p in prices:
            max_profit = max(max_profit, p-minimum_purchase)
            minimum_purchase = min(minimum_purchase, p)

        return max_profit


solution = Solution()


prices = [7, 1, 5, 3, 6, 4]
answer = solution.maxProfit(prices)
assert answer == 5, f'Got: {answer}, Expected: {5}'


prices = [7, 6, 4, 3, 1]
answer = solution.maxProfit(prices)
assert answer == 0
