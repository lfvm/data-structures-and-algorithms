
"""
100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

https://leetcode.com/problems/same-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def bfs(self, root):

        if not root: 
            return []

        res = []
        q = [root]

        while q: 

            node = q.pop(0)
            
            res.append(node.val if node else node)

            if node:
                q.append(node.left)
                q.append(node.right)
        
        return res 


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        return self.bfs(p) == self.bfs(q)