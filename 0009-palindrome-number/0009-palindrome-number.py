class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = 0
        k = x
        while k > 0:
            temp = temp * 10 + k%10
            k //= 10
        if temp == x:
            return True
        return False

        