class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)] 
        #dp[i][j] - max profit do i-tego indeksu przy j-tym stanie
        # 0 - max zysk do dnia i, gdy nie trzymam akcji
        # 1 - max zysk do dnia i, gdy mam akcję

        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            #case1 wczoraj nie trzymałem lub sprzedaję akcje z wczoraj
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            #case2 kupuję akcję dzisiaj, wczoraj trzmałem i dzisiaj dalej trzymam
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
            
        return max(dp[n-1])

        