class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: x[1] - x[0], reverse = True)

        res = 0
        current_energy = 0

        for actual, minimum in tasks:
            if current_energy < minimum:
                add_energy = minimum - current_energy
                res += add_energy
                current_energy += add_energy
            
            current_energy -= actual

        return res
        


        
