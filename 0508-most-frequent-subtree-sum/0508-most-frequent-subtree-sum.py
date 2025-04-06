# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root):
        if not root:
            return []
        frequency = {}
        max_freq = 0

        def sum_sub(root):
            nonlocal max_freq
            if not root:
                return 0
            left_sum = sum_sub(root.left)
            right_sum = sum_sub(root.right)
            current_sum = root.val + left_sum + right_sum
            frequency[current_sum] = frequency.get(current_sum, 0) + 1
            max_freq = max(max_freq, frequency[current_sum])
            return current_sum

        sum_sub(root)
        return [sum_val for sum_val, freq in frequency.items() if freq == max_freq]

            
        