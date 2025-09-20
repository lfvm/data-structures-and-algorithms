"""
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/description/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        """
            1. create a function that will merge two lists 
            2. iterate the original list, merge first two lists. 
            3. use merge result from first two items, and continue merging to that 
            list until no remaining lists are left 
        """

        def merge(list1,list2):

            dummy = ListNode()
            tmp = dummy 
            while list1 and list2: 
                if list1.val < list2.val: 
                    tmp.next = list1
                    list1 = list1.next
                else: 
                    tmp.next = list2 
                    list2 = list2.next 
                tmp = tmp.next 

            if list1: 
                tmp.next = list1 
            if list2: 
                tmp.next = list2

            return dummy.next

        if not lists: 
            return None 
        
        if len(lists) == 1: 
            return lists[0]

        sortedRes = None 
        for i in range(1,len(lists)):
            if not sortedRes: 
                l1, l2 = lists[i], lists[i-1]
                sortedRes = merge(l1,l2)
            else: 
                l2 = lists[i]
                sortedRes = merge(sortedRes, l2)

        return sortedRes


