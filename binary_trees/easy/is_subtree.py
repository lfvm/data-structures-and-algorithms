"""
572. Subtree of Another Tree

https://leetcode.com/problems/subtree-of-another-tree/description/
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
 
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """

        def check(p,q):

            if not p and not q: 
                return True
            
            if not p or not q: 
                return False 
            
            if p.val != q.val:
                return False 
            
            return check(p.left, q.left) and check(p.right, q.right)
        
        if not root or not subRoot:
            return False

        q = deque([root])
        res = False

        while q:

            node = q.popleft()
            if node: 
                    
                q.append(node.left)
                q.append(node.right)

                if node.val == subRoot.val:
                    res = check(node, subRoot)
                    if res:
                        return True
                
        return res
        
        