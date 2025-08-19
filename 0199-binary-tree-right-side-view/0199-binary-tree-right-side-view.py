# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        Q = deque([root])

        while Q:
            level_size = len(Q)

            for i in range(level_size):
                node = Q.popleft()

                if i == level_size - 1:
                    res.append(node.val)
                
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        
        return res


        