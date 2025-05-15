class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        left_profit = [0] * n
        right_profit = [0] * n

        min_price = prices[0]
        for i in range(1, n):
            left_profit[i] = max(left_profit[i - 1], prices[i] - min_price)
            min_price = min(min_price, prices[i])
        
        max_price = prices[-1]
        for i in range(n - 2, -1, -1):
            right_profit[i] = max(right_profit[i + 1], max_price - prices[i])
            max_price = max(max_price, prices[i])

        maxi_total = 0
        for i in range(n):
            maxi_total = max(maxi_total, left_profit[i] + right_profit[i])
        
        return maxi_total