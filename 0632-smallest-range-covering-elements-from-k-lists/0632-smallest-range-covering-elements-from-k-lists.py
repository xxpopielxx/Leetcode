import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        current_max = -float("inf")

        for i in range(len(nums)):
            val = nums[i][0]
            heapq.heappush(heap, (val, i, 0)) #value, index of list, index of val in list
            if val > current_max:
                current_max = val

        best_range = [-float("inf"), float("inf")]

        while True:
            val, i, j = heapq.heappop(heap)

            if current_max - val < best_range[1] - best_range[0]:
                best_range = [val, current_max]

            if j+1 == len(nums[i]): # robie break bo jeśli dojdzie do tego że ostatni element jakiejś
            # listy jest aktualnie najlniejszy to nie ma co sorawdzac dalej w sensie nie ma co brac
            # kolejnych elementów innych list no bo są one większe od tych co już mamy takze przedział
            # nie może byc mniejszy
                break

            next_val = nums[i][j+1]
            heapq.heappush(heap, (next_val, i, j+1))
            if next_val > current_max:
                current_max = next_val

        return best_range       