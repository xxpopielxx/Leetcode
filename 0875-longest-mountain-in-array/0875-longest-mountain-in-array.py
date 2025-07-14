class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0

        maxi = 0
        i = 1
        
        while i < n-1:
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]: #znajduje wierzchołek góry

                left = i-1
                while left >= 0 and arr[left] < arr[left + 1]: # rozszerzam w lewo
                    left -= 1

                right = i+1
                while right < n and arr[right] < arr[right - 1]: #rozszerzam w prawo
                    right += 1
                
                current = right - left - 1 #wyliczam długość góry
                maxi = max(maxi, current)
                i = right #przesuwam do righta bo nie ma sensu iterować do niego
            else:
                i += 1 #przesuwam jeśli nie wierzchołek

        return maxi


        
        