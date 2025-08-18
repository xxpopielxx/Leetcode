# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        def dfs(node, current_sum):
            if not node:
                return 0
            current_sum += node.val
            path_cnt = 1 if current_sum == targetSum else 0

            path_cnt += dfs(node.left, current_sum)
            path_cnt += dfs(node.right, current_sum)

            return path_cnt
        
        total = dfs(root, 0)
        total += self.pathSum(root.left, targetSum)
        total += self.pathSum(root.right, targetSum)

        return total

            
        