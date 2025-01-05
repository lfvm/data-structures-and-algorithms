"""
695. Max Area of Island
https://leetcode.com/problems/max-area-of-island/description/

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.


"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    
        if not grid or not grid[0]:
            return 0 
        
        rows, cols = len(grid), len(grid[0])
        visit = set()

        res = 0 

        def explore(r,c):

            rowInbound = r >= 0 and r < rows
            colInbound = c >= 0 and c < cols 

            if (
                not rowInbound or not colInbound
                or (r,c) in visit or 
                grid[r][c] == 0
            ):
                return 0 
            
            area = 1 
            visit.add((r,c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions: 
                area += explore(r + dr, c + dc)
                
            return area


        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == 1:
                    area = explore(r,c)
                    res = max(res,area)

        return res   