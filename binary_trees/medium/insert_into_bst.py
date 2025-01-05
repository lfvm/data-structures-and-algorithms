"""
701. Insert into a Binary Search Tree
https://leetcode.com/problems/insert-into-a-binary-search-tree/

Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root: 
            root = TreeNode(val)
            return root

        def doInsert(root, val):

            if not root: 
                root = TreeNode(val)
                return root

            if val < root.val: 
                if not root.left:
                    root.left = TreeNode(val)
                    return
                doInsert(root.left,val)
            else: 
                if not root.right:
                    root.right = TreeNode(val)
                    return 
                doInsert(root.right,val)

        doInsert(root,val)
        return root            
        

