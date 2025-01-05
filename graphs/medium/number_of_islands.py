"""
200. Number of Islands
https://leetcode.com/problems/number-of-islands/description/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        """
            We want to run a dfs or bfs algorithm on places in the grid with a 1. 

            however we only want to run this algorithm if the coordinate was not visited 
            before. that way we prevent incrementing the number of islands on adjacent nodes 
        """

        if not grid: 
            return 0 

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        res = 0 


        def explore(r,c):

            rowInBounds = r >= 0 and r < ROWS
            colInbounds = c >= 0 and c < COLS

            if (
                (r,c) in visited 
                or not rowInBounds
                or not colInbounds
                or grid[r][c] == "0"
            ): 
                return 
            
            visited.add((r,c))

            explore(r,c+1)
            explore(r,c-1)
            explore(r+1,c)
            explore(r-1,c)


        for r in range(ROWS):
            for c in range(COLS):

                if grid[r][c] == "1" and (r,c) not in visited:     
                    res+= 1 
                    explore(r,c)

        
        return res 

  

