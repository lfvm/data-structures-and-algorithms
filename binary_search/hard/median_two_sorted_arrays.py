"""
4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/description/


Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        
        def merge():

            res = []
            l,r = 0,0 
            while l < len(nums1) and r < len(nums2):

                if nums1[l] > nums2[r]:
                    res.append(nums2[r])
                    r += 1 
                else: 
                    res.append(nums1[l])
                    l += 1 

            while l < len(nums1):
                res.append(nums1[l])
                l += 1 

            while r < len(nums2):   
                res.append(nums2[r])
                r += 1 
            return res 

        completeList = merge()
        mid = len(completeList)  // 2
        print(mid)

        return float(completeList[mid]) if len(completeList) % 2 != 0 else (completeList[mid] + completeList[mid-1]) / 2 
