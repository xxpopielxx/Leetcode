class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = []
        maxi = 0
        valid_start = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i) 
            else:
                if not stack: #jesli pusty to resetuje valid_start
                    valid_start = i + 1
                else:
                    stack.pop() #usuwam odpowiednik (
                    if not stack: #jesli po usunięciu stack pusty no to valid jest s[valid_start, i]
                        current = i - valid_start + 1
                    else:  #jeśli nie pusty no to valid jest s[stack[-1] + 1, i]
                        current = i - stack[-1] 
                    maxi = max(maxi, current)
        
        return maxi

        