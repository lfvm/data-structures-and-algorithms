"""
230. Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
"""

class solution:
 
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        ktSmallest = 0 
        k = k

        def inorder(root):
            nonlocal k 
            nonlocal ktSmallest
            if not root: 
                return 
            
            inorder(root.left)
            
            if k == 1:
                ktSmallest = root.val
            k-=1

            inorder(root.right)
        inorder(root)
        return ktSmallest

    def kthSmallestIterative(self, root: Optional[TreeNode], k: int) -> int:

        res = 0 
        stack = []
        curr = root

        while curr or stack: 
            
            # Go to leftmost node 
            while curr:
                stack.append(curr)
                curr = curr.left 

            # Found a smallest element
            curr = stack.pop()
            k-= 1
            if k == 0 and curr:
                return curr.val
            
            # Start going to right subpart of the tree
            curr = curr.right

        return res


