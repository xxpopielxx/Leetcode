import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        def maxOfSubarrays(arr, k):
            n = len(arr)
            res = []
            heap = []
            for i in range(0, k):
                heapq.heappush(heap, (-arr[i], i))

            res.append(-heap[0][0])
            for i in range(k, len(arr)):

                heapq.heappush(heap, (-arr[i], i))
                while heap[0][1] <= i - k:
                    heapq.heappop(heap)

                res.append(-heap[0][0])

            return res
        return maxOfSubarrays(nums, k)