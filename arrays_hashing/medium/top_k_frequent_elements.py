
import collections
"""
Top K Elements in List

Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.
You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # array where each index represent the frequencies of occurances in nums
        # it is a list of lists because many elements can have the same number of frequencies 
        # In original array
        helper_counter = [[] for i in range(len(nums) + 1)]
        frequencies = collections.Counter(nums)

        for key in frequencies:
            helper_counter[frequencies[key]].append(key)

        ans = []

        for i in range(len(helper_counter) - 1, -1, -1):  
            for num in helper_counter[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans

        return ans 