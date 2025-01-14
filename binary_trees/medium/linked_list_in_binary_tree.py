"""
1367. Linked List in Binary Tree

https://leetcode.com/problems/linked-list-in-binary-tree/description/
Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

 

Example 1:



Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.  
Example 2:



Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Example 3:

Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.

"""


class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        

        def check(root, head):

            # We reached end of the list. List can be either whole subtree of the tree 
            # Or just a part so we can return True
            if not head: 
                return True 
            
            if not root or root.val != head.val: 
                return False 
            
            # List can be either on left side or right side
            return check(root.left, head.next) or check(root.right, head.next)
        


        q = deque([root])
        res = False
        while q: 
            currRoot = q.popleft()

            if not currRoot: 
                continue 
            
            if currRoot.val == head.val: 
                res = check(currRoot, head)
            
                if res: 
                    return True

            q.append(currRoot.left)
            q.append(currRoot.right)
        
        return res
