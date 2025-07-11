class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if not prices:
            return 0

        hold = [0] * n
        sold = [0] * n
        rest = [0] * n

        hold[0] = -prices[0]
        sold[0] = -float("inf")
        rest[0] = 0

        for i in range(1,n):
            hold[i] = max(hold[i-1], rest[i-1] - prices[i])
            sold[i] = hold[i-1] + prices[i]
            rest[i] = max(sold[i-1], rest[i-1])
        
        return max(sold[-1], rest[-1])

           


        