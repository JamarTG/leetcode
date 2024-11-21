# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = 0
        self.count = 0

        def inorder_traversal(root):
            if not root:
                return []

            inorder_traversal(root.left)
            
            self.count += 1

            if self.count == k:
                self.result = root.val

            inorder_traversal(root.right)

            
        
        inorder_traversal(root)        
        return self.result