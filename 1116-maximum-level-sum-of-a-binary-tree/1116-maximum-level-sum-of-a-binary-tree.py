# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return
        maxi = root.val
        max_lvl = 1
        Q = deque([(root, 1)])

        while Q:
            level_size = len(Q)
            current_sum = 0
            for i in range(level_size):
                node, lvl = Q.popleft()
                current_sum += node.val

                if node.left:
                    Q.append((node.left, lvl + 1))
                if node.right:
                    Q.append((node.right, lvl + 1))
            
            if current_sum > maxi:
                maxi = current_sum
                max_lvl = lvl
        
        return max_lvl

        