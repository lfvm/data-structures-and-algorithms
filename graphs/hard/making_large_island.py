"""
827. Making A Large Island
https://leetcode.com/problems/making-a-large-island/description/

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

"""

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        """

            To solve this problem we will precompute first the area of all islands. 

            To do this we need to mark an island with an id to know to which island a cell belongs to. 
            We can do it with a simple counter and marking the island with our current counter. 

            Then we search for all 0s and look for its neighbors in the four directions. Since islands 
            Have been counted at this point we can add the value of all neighboring islands 
        """


        ROWS,COLS = len(grid), len(grid[0])
        visit = set()

        def getArea(r,c, islandId):

            if ( 
                min (r,c) < 0 
                or r >= ROWS or c >= COLS or
                (r,c) in visit 
                or grid[r][c] != 1
            ):  
                return 0 
            visit.add((r,c))
            grid[r][c] = islandId
            area = 1 
            dirs = [(0,1),(0,-1),(1,0),(-1,0)]
            for dx,dy in dirs: 
                area += getArea(r+dx,c+dy, islandId)
        
            return area 

        def connect(r,c, islands): 
            area = 1  
            visited = set()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = r + dx, c + dy
                if 0 <= new_r < ROWS and 0 <= new_c < COLS:
                    islandId = grid[new_r][new_c]
                    if islandId not in visited:
                        area += islands[islandId]
                        visited.add(islandId)
            return area


        # Get all the areas of the grid. Use the label to mark a cell that belongs to an island 
        label = 2 
        islands = defaultdict(int)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: 
                    islands[label] = getArea(r,c,label)
                    label += 1      

        # If no islands are available our curr max is 0 
        res = 0 if not islands else max(islands.values())

        # Try to connect islands 
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    res = max(res,connect(r,c,islands))

        return res