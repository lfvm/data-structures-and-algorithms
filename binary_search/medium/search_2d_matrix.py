"""
Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/description/

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.


"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        #Binary search to find the row 
        l,r = 0, len(matrix) - 1
        target_row = None 

        while l <= r: 

            m = l + ((r - l) // 2)      
            row = matrix[m]
            # We have found the target row 
            if row[-1] >= target and row[0] <= target: 
                target_row = row 
                break
            
            if row[0] > target: 
                r -= 1
            elif row[0] < target: 
                l += 1 
        
        if not target_row: 
            return False
        
        l,r = 0, len(target_row) - 1  
        while l<=r:

            m = l + ((r - l) // 2)          
            if target_row[m] == target:
                return True

            elif target_row[m] > target: 
                r-=1 
            else:
                l +=1
        
        return False


