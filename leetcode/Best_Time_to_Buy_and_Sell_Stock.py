# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('INF')
        profit = 0
        for i in prices:
            if i < buy: buy = i
            if i - buy > profit: profit = i - buy
        return profit