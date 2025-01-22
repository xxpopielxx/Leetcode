class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        T = s.split()
        n = len(T)
        return len(T[n -1])
        