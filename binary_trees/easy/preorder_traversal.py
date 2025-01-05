"""
144. Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/description/

Input: root = [1,null,2,3]
Output: [1,2,3]
Explanation:


Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [1,2,4,5,6,7,3,8,9]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # Recursive approach 
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        def preorder(root):

            if not root: 
                return 
            
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)
        
        preorder(root)
        return res

    def preorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        stack = []
        curr = root

        while curr or stack:

            if curr: 
                res.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else: 
                curr = stack.pop()
        
        return res