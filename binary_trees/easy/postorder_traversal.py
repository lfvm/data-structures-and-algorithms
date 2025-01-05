"""
145. Binary Tree Postorder Traversal
https://leetcode.com/problems/binary-tree-postorder-traversal/description/

Given the root of a binary tree, return the postorder traversal of its nodes' values.
Example 1:

Input: root = [1,null,2,3]

Output: [3,2,1]

Explanation

"""

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        def postorder(root):

            if not root: 
                return 
            
            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        postorder(root)
        return res
        