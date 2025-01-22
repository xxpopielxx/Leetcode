class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                result[i] = True

        return result
        