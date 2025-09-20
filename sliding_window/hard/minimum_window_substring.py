"""
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/description/

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


"""

class Solution:

    def minWindow(self, s: str, t: str) -> str:
      
        if t == "":
            return ""

        countT, window = {}, {}
        # Get all counts for t 
        for c in t: 
            countT[c] = countT.get(c,0) + 1
        
        # For each window in the string we need to check that 
        # We have the same ammount of chars in T for it to be a 
        # possible soultion. Have represents the current chars in the 
        # window, while need is the count of all the letters we need
        # To satisfy t 
        have, need = 0, len(countT)
        l = 0 

        res, resLen = [-1,-1] , float("inf") # res represents left and right pointer 

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0) + 1

            if c in countT and window[c] == countT[c]: 
                have += 1
            
            # this means we are currently in a possible solution
            # We need the shortes substring so continue shrinking our window 
            while have == need: 
                #update our result 
                if (r-l) + 1 < resLen:
                    res = [l,r]
                    resLen = (r-l) +1
                window[s[l]] -= 1
                
                # Since we removed a val, it is possible that we removed 
                # A val we need. So we update our have var 
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -=1 
                l +=1 


        l,r = res 
        return s[l:r+1] if resLen != float("inf") else ""

