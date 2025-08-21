import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        left = [] #lewy min heap
        right = [] #prawy min heap
        min_sum = 0

        left_idx = 0
        right_idx = n - 1

        # Inicjalizacja lewego i prawego heapa
        for _ in range(candidates):
            if left_idx <= right_idx: #zeby się nie nachodziło
                heapq.heappush(left, costs[left_idx]) #dodaje lewy i prawy na raz candidates razy 
                left_idx += 1
            if left_idx <= right_idx:
                heapq.heappush(right, costs[right_idx])
                right_idx -= 1

        for _ in range(k):
            # Sprawdzamy który heap ma mniejszy element
            left_min = left[0] if left else float("inf")
            right_min = right[0] if right else float("inf")
            
            if left_min <= right_min:
                min_sum += heapq.heappop(left)
                # Dodajemy nowy element do lewego heapa jeśli są jeszcze elementy
                if left_idx <= right_idx:
                    heapq.heappush(left, costs[left_idx])
                    left_idx += 1
            else:
                min_sum += heapq.heappop(right)
                # Dodajemy nowy element do prawego heapa jeśli są jeszcze elementy
                if left_idx <= right_idx:
                    heapq.heappush(right, costs[right_idx])
                    right_idx -= 1
        
        return min_sum