class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        if n < 3:
            return 0

        n = len(nums)

        cnt = 0

        for i in range(n-1, 1, -1):
            c = nums[i]
            
            left = 0
            right = i-1

            while left < right:
                a = nums[left]
                b = nums[right]

                if a + b > c:
                    cnt += (right - left)
                    right -= 1
                    
                else:
                    left += 1
        return cnt        