class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def lis(nums):
            tails = []
            for num in nums:
                left, right = 0, len(tails)
                while left < right:
                    mid = (left + right) // 2
                    if tails[mid] < num:
                        left = mid + 1
                    else:
                        right = mid
                if left == len(tails):
                    tails.append(num)
                else:
                    tails[left] = num
            return len(tails)
    

        envelopes.sort(key=lambda x: (x[0], -x[1]))
    
        heights = [envelopes[i][1] for i in range(len(envelopes))]
        return lis(heights)