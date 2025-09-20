
"""
143. Reorder List
https://leetcode.com/problems/reorder-list/description/

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:



    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        #Step 1 split the list in half
        #Step 2 reverse the second part of the list
        #Step 3 merge both lists 

        slow, fast = head, head.next 

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next 

        # Next node from middle 
        secondList = slow.next
        #Break the list 
        slow.next = None
        
        #reverse 
        prev = None 
        tmp = secondList
        while tmp: 

            nextNode = tmp.next 
            tmp.next = prev 
            prev = tmp 
            tmp = nextNode
        
        secondList = prev

        #Merge two halfs    
        l1, l2 = head, secondList 
        while l2: 

            tmp1,tmp2 = l1.next ,l2.next
            l1.next = l2
            l2.next = tmp1
            l1,l2 = tmp1, tmp2
        return l1  
            
        