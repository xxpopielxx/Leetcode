class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        times = {}
        for num in arr:
            times[num] = times.get(num, 0) + 1
        
        n = len(times.values())
        m = len(set(times.values()))

        return n == m
