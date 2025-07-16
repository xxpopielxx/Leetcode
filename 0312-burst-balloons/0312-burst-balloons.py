class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n =len(nums)
        dp = [[0] * n for _ in range(n)] #dp[i][j] - maksymalna ilość zebrana przebijająć balony od i do j

        for length in range(1, n-1): #wybieram długość
            for left in range(1, n-length):#wybieram lewy kraniec
                right = left + length - 1 #obliczam prawy kraniec dla danej długości
                for i in range(left, right + 1): #wybieram który pomiędzy nimi będzie ostatni do przebicia
                    dp[left][right] = max(dp[left][right], nums[left-1] * nums[i] * nums[right + 1] +
                    dp[left][i-1] + dp[i+1][right])
                    #aktualizuje: i-ty który wybrałem do przebicia jako ostatni * krańce od left i right 
                    # + to co jest pomiędzy left i i oraz i i right
        
        return dp[1][n-2]
        