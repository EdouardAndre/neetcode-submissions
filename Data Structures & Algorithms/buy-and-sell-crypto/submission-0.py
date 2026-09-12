class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        i = 1
        while i < len(prices):
            if min_price > prices[i]:
                min_price = prices[i]
            if prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
            i +=1
        return max_profit

        
        