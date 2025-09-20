"""
79. Word Search
https://leetcode.com/problems/word-search/description/
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
            Run a dfs. Use a visited path set to keep track of cells we have seen 
            keep track of the current letter we are searching in the word string.

            If current letter in path is not the letter we are searching, then start 
            another path.

            If we reach the end of the word we return true

        """

        ROWS,COLS = len(board), len(board[0])
        visitedPath = set()

        def dfs(r,c,i):

            if i == len(word):
                return True 
            
            if (
                r not in range(ROWS) or 
                c not in range(COLS)
                or word[i] != board[r][c]
                or (r,c) in visitedPath
            ):
                return False

            visitedPath.add((r,c))

            result = ( dfs(r+1,c, i+1)
            or  dfs(r-1,c, i+1)
            or dfs(r,c+1, i+1)
            or dfs(r,c-1, i+1) ) 
            visitedPath.remove((r,c))
            return result


        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        
        return False