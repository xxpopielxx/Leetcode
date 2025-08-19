# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        def dfs(node, direction, length):
            if not node:
                return 

            self.max_length = max(self.max_length, length)

            if direction == "left":
                dfs(node.left, "right", length + 1) #continue
                dfs(node.right, "left", 1) #start new path
            else:
                dfs(node.right, "left", length + 1) #continue 
                dfs(node.left, "right", 1) #start new path
            
        if root:
            dfs(root.left, "right", 1)
            dfs(root.right, "left", 1)
        
        return self.max_length