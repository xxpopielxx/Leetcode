from math import sqrt

class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                res = sqrt(a**2 + b**2)
                if res.is_integer() and res <= n:
                    cnt += 2 
        return cnt


