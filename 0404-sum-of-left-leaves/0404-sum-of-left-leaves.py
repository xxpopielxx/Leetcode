# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        
        def is_leaf(node):
            return not node.left and not node.right

        stack = [root]
        total = 0

        while stack:
            node = stack.pop()
            if node.left:
                if is_leaf(node.left):
                    total += node.left.val
                else:
                    stack.append(node.left)
            if node.right:
                if not is_leaf(node.right):
                    stack.append(node.right)
        return total


        