import math
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets == 1:
            return 0
        tests = minutesToTest // minutesToDie
        T = tests + 1
        x = 0
        total = 1  # T^0
        while total < buckets:
            total *= T
            x += 1
        return x