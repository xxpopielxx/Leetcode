class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        res = 0
        current = 0
        for i in range(n):
            current += gain[i]
            res = max(res, current)

        return res
        