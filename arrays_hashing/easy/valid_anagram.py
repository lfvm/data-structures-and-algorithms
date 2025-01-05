"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/description/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        sCount, tCount = {}, {}

        for sChar, tChar in zip(s,t):
            sCount[sChar] = sCount.get(sChar,0) + 1
            tCount[tChar] = tCount.get(tChar,0) + 1


        # for key in sCount.keys():

        #     if key not in tCount or sCount[key] != tCount[key]:
        #         return False

        # return True 

        return sCount == tCount


