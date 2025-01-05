"""
Permutation String
https://neetcode.io/problems/permutation-string

You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

Input: s1 = "abc", s2 = "lecabee"

Output: true
Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:

Input: s1 = "abc", s2 = "lecaabee"

Output: false

"""


class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1Freqs = {}
        for char in s1:
            s1Freqs[char] = 1 + s1Freqs.get(char,0)

        s2Freqs = {}
        windowSize = len(s1)
        l=0
        for r in range(len(s2)):
            
            s2Freqs[s2[r]] = 1 + s2Freqs.get(s2[r],0)

            if r-l +1 == windowSize:

                if s2Freqs == s1Freqs:
                    return True
                
                else:
                    s2Freqs[s2[l]] -=1 
                    if s2Freqs[s2[l]] <= 0:
                        del s2Freqs[s2[l]]

                    l+=1
        
        return False



