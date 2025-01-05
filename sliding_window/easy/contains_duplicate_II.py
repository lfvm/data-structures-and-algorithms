"""
219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/description/

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Input: nums = [1,2,3,1], k = 3
Output: true


Input: nums = [1,2,3,1,2,3], k = 2
Output: false

"""


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:


        window = set()
        l = 0 

        for r in range(len(nums)):
            if abs(l-r) > k:
              window.remove(nums[l])
              l += 1

            if nums[r] in window:
                return True

            window.add(nums[r])   

        return  False

