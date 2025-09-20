"""
1143. Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/description/


Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # 2D Dynamic programing kind of problem
        # Bottom up approach 
        dp = [[0 for _ in range(len(text2) +1 )] for _ in range(len(text1) +1)]

        for r in range(len(text1) -1,-1,-1):
            for c in range(len(text2) -1,-1,-1):

                if text1[r] == text2[c]:
                    # Sum one because of current match and go to diagonal value
                    dp[r][c] = 1 + dp[r+1][c+1]
                else:
                    #Take the max of the bottom or right value 
                    dp[r][c] = max(dp[r+1][c], dp[r][c+1])

        return dp[0][0]