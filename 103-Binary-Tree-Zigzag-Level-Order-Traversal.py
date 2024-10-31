# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        res = []
        reverse = True 
        
        queue = [root]

        while queue:
            reverse = not reverse
            level = [node.val for node in queue]
            
            if reverse: 
                res.append(level[::-1])
            else:
                res.append(level)
        
            for idx in range(len(queue)):
                node = queue.pop(0)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return res
            
