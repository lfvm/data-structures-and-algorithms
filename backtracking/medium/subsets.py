"""
78. Subsets
https://leetcode.com/problems/subsets/description/

Given an integer array nums of unique elements, return all possible 
subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

"""

#Time complexity O(n * 2**n) memory O(n)
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        res = []
        currSubset = []

        def dfs(i):

            if i >= len(nums):
                res.append(currSubset.copy())
                return

            #Decision to use current num
            currSubset.append(nums[i])
            dfs(i+1)

            #Decision to not use currentNum 
            currSubset.pop()
            dfs(i+1)

        
        dfs(0)
        return res