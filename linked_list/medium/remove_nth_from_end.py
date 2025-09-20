"""
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
Given the head of a linked list, remove the nth node from the end of the list and return its head. 
Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        """
            Using two pointers if we shift the right one exactly n times and then we shift both 
            pointers at the same time. By the time right is out of bounds left will be exactly 
            in the node we need to delete. 

            Since we will loose reference of past node, we can use a dummy node where left will start 
        """


        dummy = ListNode()
        dummy.next = head 
        right = head 
        left = dummy 

        while right and n > 0: 
            right = right.next 
            n-=1 

        #Traverse until right is out of bounds 
        while right: 
            right = right.next 
            left = left.next
        
        #Delete 
        left.next = left.next.next 

        return dummy.next
        