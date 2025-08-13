class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 0
        max_length = 0
        cnt = k

        for j in range(n):
            if nums[j] == 0:
                cnt -= 1
            
            while cnt < 0:
                if nums[i] == 0:
                    cnt += 1
                i += 1
            
            max_length = max(max_length, j - i + 1)
        
        return max_length


 
                    


