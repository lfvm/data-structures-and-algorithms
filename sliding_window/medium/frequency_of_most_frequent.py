"""
1838. Frequency of the Most Frequent Element
https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/


The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

 

Example 1:

Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.
Example 2:

Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.

"""


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        """
        Key Idea:
        - We sort the array so that we can focus on making smaller numbers equal to the biggest number in a given window.
        - We use a sliding window approach 


        1. Start with two pointers: left and right (expanding the window).
        2. Keep track of the total sum of numbers in the window.
        3. At every step, check if we can convert all numbers in the window to match the rightmost number.
            
            Formula: max num * window size should be at most total sum + k
            * If it’s possible, expand the window (move right).
            * If not, shrink the window (move left) until it becomes valid.
        
        4. Keep track of the maximum window size found.
        """

        nums.sort()
        res = 0 
        l = 0
        curSum = 0  
        for r in range(len(nums)):

            curSum += nums[r]
            windowLenght = (r-l) + 1

            while nums[r] * windowLenght > curSum + k:
                curSum -= nums[l]
                l+=1 
                windowLenght = (r-l) + 1
                
            res = max(res, (r-l+1 ))
        return res
