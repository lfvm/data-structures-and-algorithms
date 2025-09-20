"""
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/description/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        """
            Notice how for any given number, lets say three for example 
            we are going to neeed to have at least 3 opening parenthesis and at 
            least 3 closing for the solution to be valid. 

            Running a backtracking solution is ideal heare

            On each step we need to decide wether we add an opening or a closing parenthesis

            We can add opening as long as it is less than 3 in this example.

            We can only add closing as long as the number of closing is less than the opening


            [())] -> invalid because we have 1 opening and 2 clossing
            [()()] -> valid cause we put the same amount of open and close
        """

        res = []
        stack = []
        def backtrack(nOpen, nClosed):

            if nOpen == n and nClosed == n:
                # we just finished with all combinations
                res.append("".join(stack))
                return 
            
            # Add open 
            if nOpen < n:   
                stack.append("(")
                backtrack(nOpen +1, nClosed)
                stack.pop()

            if nClosed < nOpen: 
                stack.append(")")
                backtrack(nOpen, nClosed + 1)
                stack.pop()
        
        backtrack(0,0)
        return res
