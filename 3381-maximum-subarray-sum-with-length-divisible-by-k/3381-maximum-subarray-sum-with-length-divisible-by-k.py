class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        min_prefix = [float('inf')] * k
        min_prefix[0] = 0
        
        current_sum = 0
        max_sum = -float('inf')
        
        for i, num in enumerate(nums):
            current_sum += num

            current_length = i + 1
            remainder = current_length % k

            if min_prefix[remainder] != float('inf'):
                max_sum = max(max_sum, current_sum - min_prefix[remainder])
            
            min_prefix[remainder] = min(min_prefix[remainder], current_sum)
            
        return max_sum