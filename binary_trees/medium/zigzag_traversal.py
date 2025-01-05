"""
103. Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/?envType=problem-list-v2&envId=breadth-first-search

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between). 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []

"""


from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root: 
            return []
        
        res = []
        q = deque([root])

        left_to_right = True

        while q: 

            level_count = len(q)
            level = []

            for i in range(level_count):

                node = q.popleft()
                level.append(node.val)

                if node.left: 
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)

                
            if not left_to_right: 
                level.reverse()
            
            left_to_right = not left_to_right
            res.append(level)


        return res 