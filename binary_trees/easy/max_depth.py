
"""
Maximum Depth of Binary Tree


https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

class Solution:
    
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        
        def dfs(root):

            if not root: 
                return 0 
            
            left = dfs(root.left)
            right = dfs(root.right)


            return 1 + max(left,right)  
        
        return dfs(root)