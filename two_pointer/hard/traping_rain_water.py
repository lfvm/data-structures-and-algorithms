"""
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/description/
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        

        l, r = 0, len(height) - 1 

        maxLeft = height[l]
        maxRight = height[r]
        res = 0 

        while l<r:

            if maxLeft < maxRight: 
                l+=1 
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]
            else: 
                r-=1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]
        return res