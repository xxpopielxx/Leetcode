class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hash_set = set(nums) #moge skorzystać bo w pythonie set ma operacje O(1)
        
        res = 0
        for num in hash_set: 
            if (num-1) not in hash_set: #jeśli aktualny num może byc początkiem ciągu
                current_num = num
                current_length = 1
                while (current_num + 1) in hash_set:#jadę do końca tego ciągu
                    current_num += 1
                    current_length += 1

                res = max(res, current_length)

        return res