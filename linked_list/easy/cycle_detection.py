"""
Linked List Cycle Detection
https://neetcode.io/problems/linked-list-cycle-detection

Given the beginning of a linked list head, return true if there is a cycle in the linked list. Otherwise, return false.

There is a cycle in a linked list if at least one node in the list that can be visited again by following the next pointer.

Internally, index determines the index of the beginning of the cycle, if it exists. The tail node of the list will set it's next pointer to the index-th node. If index = -1, then the tail node points to null and no cycle exists.

Note: index is not given to you as a parameter.

Example 1:



Input: head = [1,2,3,4], index = 1

Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:



Input: head = [1,2], index = -1

Output: false
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#O(n) time and space
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        visited = set()

        curr = head

        while curr: 

            if curr.val in visited:
                return True 
            visited.add(curr.val)
            curr = curr.next

        return False

#O(n) time and O(1) space

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = slow.next

        while fast and fast.next: 

            if slow.val == fast.val:
               return True

            slow = slow.next
            fast = fast.next.next
            
        return False