"""
63. Unique Paths II
https://leetcode.com/problems/unique-paths-ii/description/


You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.


"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        M,N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * (N+1)
        dp[N-1] = 1 

        for r in reversed(range(M)):
            for c in reversed(range(N)):

                if obstacleGrid[r][c] == 1: 
                    dp[c] = 0 
                else: 
                    dp[c] = dp[c] + dp[c+1]
        
        return dp[0]
