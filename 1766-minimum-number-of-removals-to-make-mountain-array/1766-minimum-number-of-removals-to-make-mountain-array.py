class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        #LIS
        lis = [1] * n
        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i] and lis[j] + 1 > lis[i]:
                    lis[i] = lis[j] + 1

        #LDS
        lds = [1] * n
        for i in range(n-1, -1 ,-1):
            for j in range(i+1,n):
                if nums[i] > nums[j] and lds[j] + 1 > lds[i]:
                    lds[i] = lds[j] + 1
        maxi = 0
        for i in range(1, n-1):
            if lis[i] > 1 and lds[i] > 1:
                current = lis[i] + lds[i] - 1
                maxi = max(maxi, current)
        
        return n - maxi if maxi >= 3 else n - 3


        