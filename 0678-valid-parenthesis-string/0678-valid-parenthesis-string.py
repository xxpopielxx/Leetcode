class Solution:
    def checkValidString(self, s: str) -> bool:

        low = 0 #minimalna liczba nawiasów otwierających
        high = 0 #maksymalna liczba nawaisów otwierających

        for char in s:
            if char =="(":
                high += 1
                low += 1
            elif char == "*":
                low = max(low-1, 0) #traktuje jako zamykający ale nie spadam poniżej 0
                high += 1 #traktuje jako otwierjący
            else:
                low = max(low - 1, 0) #odejmuje 
                high -= 1
            
            if high < 0:
                return False
        
        return low == 0


