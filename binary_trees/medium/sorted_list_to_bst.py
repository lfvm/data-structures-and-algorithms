
"""
109. Convert Sorted List to Binary Search Tree
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """


        
        elements = []
        while head: 
            elements.append(head.val)
            head = head.next
        
        def helper(elements):
            if not elements:
                return None

            mid = len(elements) // 2
            node = TreeNode(elements[mid])
            node.left = helper(elements[:mid])
            node.right = helper(elements[mid+1: len(elements)])
            return node

        return helper(elements)


