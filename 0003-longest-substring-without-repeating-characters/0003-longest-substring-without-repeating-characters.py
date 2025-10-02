class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxi = 0
        ind = {}

        for i,ch in enumerate(s):
            if ch in ind and ind[ch] >= start:
                start = ind[ch] + 1
            ind[ch] = i
            maxi = max(maxi, i - start + 1)

        return maxi