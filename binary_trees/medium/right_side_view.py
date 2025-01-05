"""
199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/description/

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        q = collections.deque()

        if root:
            q.append(root)

        while q:

            rightMost = None
            for i in range(len(q)):
                
                node = q.popleft()
                rightMost = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(rightMost.val)
        
        return res