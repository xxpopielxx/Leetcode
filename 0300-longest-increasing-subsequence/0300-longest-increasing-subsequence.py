class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            left, right = 0, len(stack) - 1
            while left <= right:
                mid = (left + right) // 2
                if stack[mid] >= num:
                    right = mid - 1
                else:
                    left = mid + 1
            if left < len(stack):
                stack[left] = num
            else:
                stack.append(num)
        return len(stack)