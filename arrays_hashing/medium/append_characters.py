"""
2486. Append Characters to String to Make Subsequence
https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/

You are given two strings s and t consisting of only lowercase English letters.
Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.



Example 1:

Input: s = "coaching", t = "coding"
Output: 4
Explanation: Append the characters "ding" to the end of s so that s = "coachingding".
Now, t is a subsequence of s ("coachingding").
It can be shown that appending any 3 characters to the end of s will never make t a subsequence.
Example 2:

Input: s = "abcde", t = "a"
Output: 0
Explanation: t is already a subsequence of s ("abcde").
Example 3:

Input: s = "z", t = "abcde"
Output: 5
Explanation: Append the characters "abcde" to the end of s so that s = "zabcde".
Now, t is a subsequence of s ("zabcde").
It can be shown that appending any 4 characters to the end of s will never make t a subsequence.
"""


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        

        # 1. pointer on t representing satisfaction of cur char
        # 2. iterate s. If satisfies pointer, then move pointer to next char 
        # 3. if we have finished s, then we need to append the remaining chars in t 
        # 4. if we finished t, then its already satisfied 


        indexOfcharToSatisfy = 0
        for char in s:

            if indexOfcharToSatisfy >= len(t):
                return 0
            
            if char == t[indexOfcharToSatisfy]: 
                indexOfcharToSatisfy += 1
            
        
        return (len(t) - indexOfcharToSatisfy )


