class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums)
        cnt = 0
        if l == 1 and nums[0] == target:
            return 0
        while target > nums[cnt]:
            cnt += 1
            if cnt == l:
                return l
        if target == nums[cnt - 1]:
            return cnt - 1
        else:
            return cnt

        