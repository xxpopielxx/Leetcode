class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        end = 0
        longest = 0

        for i in range(len(nums) - 1):
            longest = max(longest, i + nums[i]) 

            if i == end:
                jumps += 1
                end = longest
        
        return jumps