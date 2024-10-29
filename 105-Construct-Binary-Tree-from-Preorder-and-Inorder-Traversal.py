# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return None
        
        inorder_root_index = inorder.index(preorder[0])
        
        inorder_left = inorder[:inorder_root_index] #1
        inorder_right = inorder[inorder_root_index + 1:] #3
        
        preorder_left = preorder[1:1+len(inorder_left)]
        preorder_right = preorder[1+len(inorder_left):]

        return TreeNode(preorder[0],self.buildTree(preorder_left,inorder_left),self.buildTree(preorder_right,inorder_right))

