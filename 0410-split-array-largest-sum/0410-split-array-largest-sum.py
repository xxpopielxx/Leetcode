class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def is_possible(max_sum): #sprawdza czy da się podzielć na m arrayów takich że ichu sumy są mniejsze lub równe max_sum
            current_sum = 0
            splits = 1 
            for num in nums :
                current_sum += num
                if current_sum > max_sum:
                    splits += 1
                    current_sum = num
                    if splits > k:
                        return False
            return True

        left = max(nums) #szukamy sum między maksymalnym elementem jeśli k=len(nums) lub suma całości jesli k = 1
        right = sum(nums)
        answer = right

        while left <= right: #binary searchem szukam tej minimalnej(maksymalnej) sumy
            mid = (left + right) // 2
            if is_possible(mid):
                answer = mid
                right = mid-1
            else: 
                left = mid + 1
        
        return answer