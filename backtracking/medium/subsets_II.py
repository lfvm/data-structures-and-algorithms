"""
90. Subsets II
https://leetcode.com/problems/subsets-ii/description/


Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        currSubset = []
    
        #will not affect time complexity since this solution is already O(n*2**n)
        nums.sort()

        def dfs(i):

            if i == len(nums):
                res.append(currSubset.copy())
                return
            

            #Use currentNumber
            currSubset.append(nums[i])
            dfs(i+1)
            currSubset.pop()

            # We do not want to include a duplicate number here
            # So we increment i until we are on a new number 
            while i < len(nums) -1  and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1)
        
        dfs(0)
        return res