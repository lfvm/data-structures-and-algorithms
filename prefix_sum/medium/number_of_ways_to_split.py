"""
2270. Number of Ways to Split Array

https://leetcode.com/problems/number-of-ways-to-split-array/description/?envType=daily-question&envId=2025-01-03

You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums.


Input: nums = [10,4,-8,7]
Output: 2
Explanation: 
There are three ways of splitting nums into two non-empty parts:
- Split nums at index 0. Then, the first part is [10], and its sum is 10. The second part is [4,-8,7], and its sum is 3. Since 10 >= 3, i = 0 is a valid split.
- Split nums at index 1. Then, the first part is [10,4], and its sum is 14. The second part is [-8,7], and its sum is -1. Since 14 >= -1, i = 1 is a valid split.
- Split nums at index 2. Then, the first part is [10,4,-8], and its sum is 6. The second part is [7], and its sum is 7. Since 6 < 7, i = 2 is not a valid split.
Thus, the number of valid splits in nums is 2.

"""

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        """
        Step 1: Build a prefix sum of the array 
        [10,4,-8,7]
        [10,14,6,13] -> our prefix sum  

        Step 2 iterate each index of our prefix sum 
        In each step check if conditions ara valid

        10 -> 13 - 10 = 3 -> valid 
        14 -> 13 - 14 = 1 -> valid 
        6 -> 13 -6 = 7    -> invalid    

        Step 3: Count valid conditions and return number of valid conditions 
        """    
        
        res = 0 
        for i in range(1, len(nums)): 
            nums[i] = nums[i-1] + nums[i]

        for i in range(len(nums) -1 ):
            curr = nums[i]

            # We do not want to take into account the left part of the array 
            # That is why we substract 
            rightSum = nums[-1] - curr
            if curr >= rightSum:
                res += 1 
        
        return res
