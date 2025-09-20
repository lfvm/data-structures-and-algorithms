"""
1448. Count Good Nodes in Binary Tree
https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        
        def dfs(root, curMax):

            if not root:
                return 0 
            
            res = 0 
            if root.val >= curMax: 
                curMax = root.val 
                res += 1 
            
            res += dfs(root.left, curMax)
            res += dfs(root.right, curMax) 

            return  res
        

        return dfs(root, float("-inf"))
