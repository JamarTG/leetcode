# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        \\\
        :type root: Optional[TreeNode]
        :rtype: str
        \\\
        if not root:
            return \\
        
        left = right = \\
        
        
        if root.left or (not root.left and root.right):
            left = \(\ + self.tree2str(root.left) + \)\
       
        
        if root.right:
            right = \(\ + self.tree2str(root.right) + \)\



        return str(root.val) + left + right