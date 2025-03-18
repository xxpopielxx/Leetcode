from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        buckets = [[] for _ in range(n+1)]

        for num, freq in counter.items():
            buckets[freq].append(num)
        
        result = []
        for i in range(n, -1, -1):
            if buckets[i]:
                for num in buckets[i]:
                    result.append(num)
                    if len(result) == k:
                        return result
        return result


        
        
            

            
                
                


        