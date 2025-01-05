"""
Longest Substring Without Duplicates
https://neetcode.io/problems/longest-substring-without-duplicates


Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "zxyzxyz"

Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:
Input: s = "xxxx"
Output: 1

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0 
        ans = float("-inf")
        seen = set()

        for r in range(len(s)):

            currChar = s[r]
            while currChar in seen:
                #Move window to left
                seen.remove(s[l])
                l +=1

            seen.add(currChar)      
            ans = max(r-l+1, ans)

        return 0 if ans == float("-inf") else ans

