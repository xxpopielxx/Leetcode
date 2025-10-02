class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            return s[left+1:right]
        
        res = ""
        for i in range(len(s)):
            p1 = expand(i,i) #nieparzysty np: "aba"
            p2 = expand(i,i+1)  #parzysty np: "abba"
        
            if len(p1) > len(res):
                res = p1
            if len(p2) > len(res):
                res = p2
        
        return res
