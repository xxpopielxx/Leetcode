class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[1], -x[0]))

        a, b = -1, -1
        res = 0

        for c, d in intervals:
            #rozłączne
            if c > b:
                res += 2
                a = d-1
                b = d

            elif c > a:
                res += 1
                a = b
                b = d
    
        return res

