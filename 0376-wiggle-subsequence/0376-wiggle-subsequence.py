class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        prev_diff = nums[1] - nums[0]
        cnt = 2 if prev_diff !=0 else 1

        for i in range(2, len(nums)):
            curr_diff = nums[i] - nums[i-1]
            if (prev_diff <= 0 and curr_diff > 0) or (prev_diff >= 0 and curr_diff < 0):
                cnt += 1
                prev_diff = curr_diff
        
        return cnt


        