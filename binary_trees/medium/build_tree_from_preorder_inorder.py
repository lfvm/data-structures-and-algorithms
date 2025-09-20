"""
105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

Example 1:


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        """
            Two facts: 
                1. Ther first value in the preorder list is ALWAYS going to be the root

                2. When we find the value of our root in the inorder list. We now 
                all of the values to its left are going to be on the left part of the tree
                and all of the values to the right are going to be on the right. 
            
            So recursively:
             1 we can get the first value from the preorder list. 
             2 Find left and right childs and Build subtree. 
             3 use our next root (first value next to our curr root )
        """

        if not inorder or not preorder: 
            return None 
        
        root = TreeNode(preorder[0])

        # Values on the left of mid belong to left and viceversa on right
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root 
