class Solution:

    """
    
        Original approach to solve this problem is with a single depth first search.
        However. to achieve this we need to compute the number of ways on each step of the grid
        There is a ton of repeated work which leads to a 2**n*m time complexity.

        A better approach is to use 2d dynamic programing.
        Where we compute the sum from the very bottom and build our way up to the top.

        We can use a 2d array to store the number of ways to reach the end of the grid.
        We start from the last row and iterate from the right to the left.
        We compute the number of ways to reach the end of the grid from the current cell.
    
    """        

    def uniquePaths(self, m: int, n: int) -> int:
        
        # 2d Dynamic programming 
        prevRow = [0] * n 

        #iterate from last row from right to left 
        # Bottom up approach
        for r in range(m-1, -1, -1):
            currRow = [0] * n
            currRow[-1] = 1 # we know the last col can only go down so there is only one way to reach the end 
            for c in range(n - 2,-1,-1):
                currRow[c] = currRow[c+1] + prevRow[c]
            
            prevRow = currRow
        
        return prevRow[0]
   
   
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [0] * (n+1)
        dp[n-1] = 1 
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                dp[c] = dp[c] + dp[c+1]
        return dp[0]


    def uniquePathsDfs(self, m: int, n: int) -> int:
        def dfs(r,c):

            if (
                r not in range(m) or c not in range(n)
            ):
                return 0
            
            if (r == m-1 and c == n-1):
                return 1 
            
            return  dfs(r+1, c)  + dfs(r,c+1)
        
        return dfs(0,0)


