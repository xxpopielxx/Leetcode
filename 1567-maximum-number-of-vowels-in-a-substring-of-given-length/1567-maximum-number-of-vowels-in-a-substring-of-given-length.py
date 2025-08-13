class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        current = 0
        for i in range(k):
            if s[i] in "aeiou":
                current += 1
        res = current
        i = 0
        j = k-1

        while j < n-1:
            if s[j+1]  in "aeiou" and s[i] not in "aeiou":
                current += 1
                if current > res:
                    res = current
            elif s[j+1] not in "aeiou" and s[i] in "aeiou":
                current -= 1
            
            i += 1
            j += 1

        return res 