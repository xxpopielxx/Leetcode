class Solution:
    def removeStars(self, s: str) -> str:
        n = len(s)
        stack = []

        for i in range(n):
            if s[i] != "*":
                stack.append(s[i])
            else:
                stack.pop()
        
        res = ""
        while stack:
            res += stack.pop()
        
        return res[::-1]