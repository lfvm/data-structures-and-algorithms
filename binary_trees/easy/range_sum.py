"""
938. Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/description/

Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
"""



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """

        def recursive(root):

            if not root: 
                return 0

            res = 0

            if root.val > high: 
                res += recursive(root.left)
            elif root.val < low: 
                res += recursive(root.right)
            
            else: 
                res += root.val + recursive(root.left) + recursive(root.right)

            return res 
            
        
        return recursive(root)
    

class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """

        res = 0 
        stack = [root]

        while stack: 

            node = stack.pop()

            if node: 

                if node.val >= low and node.val <= high:
                    res+= node.val
                

                stack.append(node.left)
                stack.append(node.right)


        return res 