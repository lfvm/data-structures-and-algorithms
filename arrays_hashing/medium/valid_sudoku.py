import collections
"""
Valid Sudoku
https://leetcode.com/problems/valid-sudoku/description/


Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.

"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rFreq,cFreq = collections.defaultdict(set), collections.defaultdict(set)
        boxFreq = collections.defaultdict(set) # ((r/3, c/3))


        ROWS,COLS = len(board), len(board)


        for r in range(ROWS):
            for c in rang(COLS):

                if board[r][c] == ".":
                    continue
                    
                currentVal = board[r][c]

                if (
                    currentVal in rFreq[r] or 
                    currentVal in cFreq[c] or 
                    currentVal in boxFreq[(r//3,c//3)]
                ): 
                    return False 
                
                rFreq[r].add(currentVal)
                cFreq[c].add(currentVal)
                boxFreq[(r//3,c//3)].add(currentVal)
    
        return True