# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMin(node):
            current = node
            while current.left:
                current = current.left
            return current

        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else:
            # Node found, now delete it

            # case1, no children or one
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Case 2: Node has two children
            # smallest in right subtree
            successor = findMin(root.right) # find min
            root.val = successor.val # swap the val
            root.right = self.deleteNode(root.right, successor.val) # delete this smallest in right subtree

        return root

