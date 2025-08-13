class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        maxi = 0
        cnt = 1

        for j in range(n):
            if nums[j] == 0:
                cnt -= 1
            
            while cnt < 0:
                if nums[i] == 0:
                    cnt += 1
                i += 1
            
            maxi = max(maxi, j - i)
    
        return maxi