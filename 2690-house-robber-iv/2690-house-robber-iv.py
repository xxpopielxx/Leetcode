class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        #sprawdzam czy da się okraść min k domów takich żeby wartość była mniejsza lub równa cap
        def can_rob(cap):
            cnt = 0
            i = 0
            n = len(nums)
            while i < n:
                if nums[i] <= cap:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            
            return cnt >= k

        # binary searchem poruszam się capem i sprawdzam czy da się okraśc te minimum k domów,
        # jeśli tak no to przesuwam w lewo i sprawdzam mniejsze jeśli nie no to przesuwam w prawo
        # i sprawdzam większe
        left = min(nums)
        right = max(nums)
        res = right

        while left <= right:
            mid = (left + right) // 2
            if can_rob(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
            
        return res