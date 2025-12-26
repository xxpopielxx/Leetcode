class Solution:
    def bestClosingTime(self, customers: str) -> int:
        current_penalty = customers.count('Y')
        min_penalty = current_penalty
        best_hour = 0
        
        for i, char in enumerate(customers):
            if char == 'Y':
                current_penalty -= 1
            else:
                current_penalty += 1
            
            if current_penalty < min_penalty:
                min_penalty = current_penalty
                best_hour = i + 1
                
        return best_hour

