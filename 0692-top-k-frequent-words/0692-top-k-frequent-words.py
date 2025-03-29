class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        def merge(left, right):
            result = []
            l = r = 0
            while l  < len(left) and r < len(right):
                if left[l] < right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
            
            while l  < len(left):
                result.append(left[l])
                l += 1
            while r < len(right):
                result.append(right[r])
                r += 1
            return result

        def ms(T):
            if len(T) < 2:
                return T
            mid = len(T) // 2
            left = ms(T[:mid])
            right = ms(T[mid:])
            return merge(left, right)

        words = ms(words)
        cnt = {}
    
        for element in words:
            cnt[element] = cnt.get(element, 0) + 1
            
        top_k = [key for key, _ in sorted(cnt.items(), key=lambda item: item[1], reverse=True)[:k]]
        return top_k    



        
                
                