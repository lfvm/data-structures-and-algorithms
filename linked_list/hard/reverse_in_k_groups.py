"""
25. Reverse Nodes in k-Group
https://leetcode.com/problems/reverse-nodes-in-k-group/description/

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """ 
            Split the list in groups of lenght k. Have a pointer previous of our group 
            and a pointer one node after the group. 

            When we reverse a group we know we need to point the reverse node to the next 
            pointer after the group so we do not break the loop. 

        """

        def getKth(head,k):
            while head and k > 0: 
                head = head.next 
                k-=1 
            return head 


        dummy = ListNode(0,head)
        groupPrev = dummy 
        while True: 

            kth = getKth(groupPrev,k)
            # We reached the end of the list or we can no longer reverse 
            if not kth: 
                break 

            groupNext = kth.next 

            # Reverse our group 
            prev,curr = groupNext, groupPrev.next 
            while curr != groupNext: 
                nextN = curr.next 
                curr.next = prev 
                prev = curr 
                curr = nextN 

            tmp = groupPrev.next 
            # So our dummy node knows where the list will start 
            groupPrev.next = kth
            # Move our grou prev one node previous to next group  
            groupPrev = tmp  

        return dummy.next 




