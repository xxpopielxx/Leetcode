import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n = len(nums1)
        # Tworzymy pary (nums1[i], nums2[i]) bez użycia zip
        pairs = []
        for i in range(n):
            pairs.append((nums1[i], nums2[i]))
        
        # Sortujemy pary według nums2 w kolejności malejącej
        pairs.sort(key=lambda x: x[1], reverse=True)
        
        min_heap = []
        current_sum = 0
        max_score = 0
        
        # Iterujemy przez pary używając zwykłej pętli for
        for i in range(n):
            num1, num2 = pairs[i]
            # Dodajemy current num1 do heap i sumy
            heapq.heappush(min_heap, num1)
            current_sum += num1
            
            # Jeśli mamy więcej niż k elementów, usuwamy najmniejszy
            if len(min_heap) > k:
                smallest = heapq.heappop(min_heap)
                current_sum -= smallest
            
            # Jeśli mamy dokładnie k elementów, obliczamy score
            if len(min_heap) == k:
                score = current_sum * num2
                if score > max_score:
                    max_score = score
        
        return max_score