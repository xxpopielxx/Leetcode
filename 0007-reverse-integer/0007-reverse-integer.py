class Solution:
    def reverse(self, x: int) -> int:
        reversed_int = int(str(x)[::-1]) if x >= 0 else -int(str(x)[:0:-1])

        return reversed_int if -2**31 <= reversed_int <= 2**31 - 1 else 0



        
        


        