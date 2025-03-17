class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(T,n,i):
            max_ind = i
            l = 2*i + 1
            r = 2*i + 2
            if l < n and T[l] > T[max_ind]:
                max_ind = l
            if r < n and T[r] > T[max_ind]:
                max_ind = r
            if max_ind != i:
                T[i], T[max_ind] = T[max_ind], T[i]
                heapify(T,n,max_ind)    

        def build_max_heap(T):
            n = len(T)
            for i in range((n - 1)//2, -1, -1):
                heapify(T,n,i)

        n = len(nums)
        build_max_heap(nums)
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(nums, i, 0)
        return nums    
        

        