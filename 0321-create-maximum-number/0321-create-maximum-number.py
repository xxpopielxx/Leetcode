class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m, n = len(nums1), len(nums2)
        best_result = []

        for i in range(max(0, k - n), min(k, m) + 1):
            j = k - i
            
            subsequence1 = self.prep(nums1, i)
            subsequence2 = self.prep(nums2, j)
            
            merged = self.merge(subsequence1, subsequence2)
            
            if merged > best_result:
                best_result = merged
                
        return best_result

    def prep(self, nums, l):
        if l == 0:
            return []
            
        stack = []
        drops_left = len(nums) - l
        
        for num in nums:
            while stack and drops_left > 0 and stack[-1] < num:
                stack.pop()
                drops_left -= 1
            stack.append(num)
            
        return stack[:l]

    def merge(self, arr1, arr2):
        res = []
        while arr1 or arr2:
            if arr1 > arr2: #python działa tak ze sprawdza mi leksykograficzcznie któa jest większa potem więc nie muszę iterować
                res.append(arr1.pop(0))
            else:
                res.append(arr2.pop(0))
        return res
      