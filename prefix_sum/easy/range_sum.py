"""
303. Range Sum Query - Immutable
https://leetcode.com/problems/range-sum-query-immutable/

given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclu
"""

class NumArray:

    def __init__(self, nums: List[int]):

        self.prefix = [] 
        prefixSum = 0
        for num in nums:
            prefixSum += num
            self.prefix.append(prefixSum)

        

    def sumRange(self, left: int, right: int) -> int:
        
        rightSum = self.prefix[right]
        leftSum = self.prefix[leftSum -1]

        if left > 0: 
            return rightSum - leftSum
        return rightSum