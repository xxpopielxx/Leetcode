class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
            char = s[i]
            last[char] = i
        
        res = []
        start = 0
        end = 0
        for i in range(len(s)):
            char = s[i]

            if last[char] > end:
                end = last[char]
            
            if i == end:
                length = i - start + 1
                res.append(length)
                start = i + 1
        
        return res