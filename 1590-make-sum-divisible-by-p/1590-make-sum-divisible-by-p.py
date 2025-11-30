class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p
    
        if remainder == 0:
            return 0
    
        mod_map = {0: -1}
        
        current_sum = 0
        min_len = len(nums)
        n = len(nums)
        
        for i, num in enumerate(nums):
            current_sum = (current_sum + num) % p
            target = (current_sum - remainder) % p
            
            if target in mod_map:
                length = i - mod_map[target]
                min_len = min(min_len, length)
            
            mod_map[current_sum] = i
            
        if min_len == n:
            return -1
        else:
            return min_len