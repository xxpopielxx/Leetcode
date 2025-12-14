class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seats = [i for i, char in enumerate(corridor) if char == 'S']

        if len(seats) == 0 or len(seats) % 2 != 0:
            return 0
        
        if len(seats) == 2:
            return 1
        
        MOD = 10**9 + 7
        res = 1

        for i in range(2, len(seats), 2):
            prev_seat_index = seats[i-1]
            curr_seat_index = seats[i]

            ways = curr_seat_index - prev_seat_index

            res = (res * ways) % MOD

        return res
