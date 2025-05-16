class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        n = 0
        for char in t:
            if char == s[n]:
                n += 1
                if n == len(s):
                    return True
        return False

        