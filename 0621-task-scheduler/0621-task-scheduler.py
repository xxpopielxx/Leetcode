
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}        
        for t in tasks:
            if t not in freq:
                freq[t] = 0
            freq[t] += 1
        
        maxi = 0
        for t in freq:
            maxi = max(maxi, freq[t])
        
        how_many_maxi = 0
        for t in freq:
            if freq[t] == maxi:
                how_many_maxi += 1
        
        res = (maxi - 1) * (n+1) + how_many_maxi # ilość bloków A__ np czyli jak są 3 A no to 2 bloki + dodajemy ten brakujący,
        # po to jest to how_many_maxi żeby wiedzieć ile dodać

        if res < len(tasks):
            return len(tasks)
        return res