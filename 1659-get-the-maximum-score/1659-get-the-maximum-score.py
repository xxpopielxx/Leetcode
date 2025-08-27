class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        suma = sumb = 0
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]: #dodaje mniejszy element dlatego że mam pewność przez to że 
            # są posortowane tablice to wiem że ten mniejszy element napewno nie wystąpi już w 
            # drugiej tablicy
                suma += nums1[i]
                i += 1
            elif nums1[i] > nums2[j]:
                sumb += nums2[j]
                j += 1
            else:
                best = max(suma, sumb) + nums1[i]
                suma = sumb = best
                i += 1
                j += 1
        
        while i < len(nums1): #dodaje reszte
            suma += nums1[i]
            i += 1
        while j < len(nums2):
            sumb += nums2[j]
            j += 1

        return max(suma, sumb) % (10**9 + 7)


