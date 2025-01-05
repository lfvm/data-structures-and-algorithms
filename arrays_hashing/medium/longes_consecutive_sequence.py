"""
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/description/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        nums = set(nums)
        res = 0 

        for num in nums: 
            
            #Begining of a sequence
            if not num - 1 in nums:

                count = 1 
                tmp = num
                while tmp + 1 in nums: 
                    count += 1
                    tmp+=1

                res = max(count,res) 




        return res