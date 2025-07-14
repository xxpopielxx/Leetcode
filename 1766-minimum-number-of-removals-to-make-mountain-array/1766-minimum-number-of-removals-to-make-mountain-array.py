import bisect

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        # LIS nlogn
        lis = [1] * n
        tails = []
        for i in range(n):
            idx = bisect.bisect_left(tails, nums[i])
            if idx == len(tails):
                tails.append(nums[i])
            else:
                tails[idx] = nums[i]
            lis[i] = idx + 1
        
        # LDS nlogn
        lds = [1] * n
        tails = []
        for i in range(n-1, -1, -1):
            idx = bisect.bisect_left(tails, nums[i])
            if idx == len(tails):
                tails.append(nums[i])
            else:
                tails[idx] = nums[i]
            lds[i] = idx + 1
        
        max_mountain = 0
        for i in range(n):
            if lis[i] > 1 and lds[i] > 1:
                current_mountain = lis[i] + lds[i] - 1
                if current_mountain > max_mountain:
                    max_mountain = current_mountain
        
        return n - max_mountain if max_mountain >= 3 else n - 3


        