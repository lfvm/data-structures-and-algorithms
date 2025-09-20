"""
84. Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/description/

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """

            To solve this problem we are going to use a stack where we store 
            the height at a given index and its index. 

            We will continue adding to our stack as long as it is in ascending order 
            Since we know we can continue building a rectangle to the right 
            as long as this condition is met. 

            IF we had 6 and 1. 6 can not continue growing to its right cause one is smaller.


            Whenever we find a case where curr is smaller than top of stack. Compute the area 
            of given index and index of top. Then continue poping while this is the case. 

            Finally compute area for remaining elements in case we have ended iteration
        """

        stack = [] # pair (index, h)
        res = 0 
        n = len(heights)

        for i, height in enumerate(heights): 
            newI = i 
            while stack and stack[-1][1] > height:
                prevI, prevH = stack.pop()
                # Compute the area 
                res = max(res, prevH * (i - prevI))
                #Since current smaller number can extend to its left 
                #we want to mark the start of curr rectangle on the prev 
                #index
                newI = prevI 
                
            stack.append((newI,height))
            

        # get area for pending elements
        while stack:
            i,h = stack.pop()
            res = max(res, h * (n - i))

        return res 

