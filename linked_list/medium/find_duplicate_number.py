"""

287. Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/description/

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3


"""


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """ 
            To solve use floyds hare algorithm. 

            Since number are going to be in range 1-n (n being lenght of array)
            We can use the actual numbers to point them in other indexes of the array.
            When we have a repeated Item they will point to the same index of 
            the array. Initiating a cycle 
        """
        
        slow,fast = 0,0 
        # Find the cycle 
        while True: 
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast: 
                break 

        # We know that the distance from the begining of the array 
        # Up until the start of the cycle is going to be the same 
        # distance where our prev slow pointer was left. 
        slow2 = 0 

        while True: 
            slow2 = nums[slow2]
            slow = nums[slow]

            if slow2 == slow: 
                # We can return either of them 
                return slow
