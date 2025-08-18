# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxi = 0
        cnt = 0
        def dfs(root, maxi):
            if not root:
                return 0
            cnt = 0
            if maxi <= root.val:
                cnt += 1
                maxi = root.val
            
            cnt += dfs(root.left, maxi)
            cnt += dfs(root.right, maxi)
            return cnt
        
        return dfs(root, -float("inf"))

            
        