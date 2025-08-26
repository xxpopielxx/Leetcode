import math
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        n = len(machines)
        if total % n != 0:
            return -1
        
        target = total // n
        res = 0
        balance = 0

        for m in machines:
            diff = m - target
            balance += diff
            res = max(res, abs(balance), diff)
        
        return res

