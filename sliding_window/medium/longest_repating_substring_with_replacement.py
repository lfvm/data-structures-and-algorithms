"""
Longest Repeating Substring With Replacement
https://neetcode.io/problems/longest-repeating-substring-with-replacement

You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

Example 1:

Input: s = "XYYX", k = 2

Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:

Input: s = "AAABABB", k = 1


"""


class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        
        seen = {}
        res = 0
        l=0 

        for r in range(len(s)):
            
            seen[s[r]]  = 1 +  seen.get(s[r],0)
        
            while (r-l+1) - max(seen.values()) > k:

                seen[s[l]] -=1
                l +=1 

            res = max(res, r-l+1)
        return res 