"""
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/description/

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

"""


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0 
        currSum = 0 
        prefixSums = {0:1} # Edge case for empty subarray 

        for n in nums: 

            currSum += n 
            diff = currSum - k 

            if diff in prefixSums: 
                res += prefixSums.get(diff)

            prefixSums[currSum] = 1 +  prefixSums.get(currSum,0 )
        
        return res