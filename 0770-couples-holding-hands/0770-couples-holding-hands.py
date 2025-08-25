import math
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        position = {}

        for i in range(n): #mapuje pozycje 
            position[row[i]] = i
        
        swaps = 0

        for i in range(0, n, 2):
            x = row[i]
            if x % 2 == 0: 
                expected_partner = x + 1
            else:
                expected_partner = x - 1
            
            if row[i+1] != expected_partner:
                partner_pos = position[expected_partner] #pozycja expected_partner

                row[i+1], row[partner_pos] = row[partner_pos], row[i+1] #swapuje 
 
                position[row[i+1]] = i+1 #aktualizuje tearz własciwy partner to row[i+1] a niewłaściwy
                # to row[partner_pos]
                position[row[partner_pos]] = partner_pos

                swaps += 1
        return swaps
        