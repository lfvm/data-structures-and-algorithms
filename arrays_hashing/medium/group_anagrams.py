import collections

"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/description/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]



Solution: 

we know that an anagram is two strings with the same number of chars;

if we sort the letters, we will get a unique key that we can use in a hash map, where we will save an array with the actual word. 
Then we can do that for all letters in the input and return the values of the hash map.

A more efficient approach to prevent sorting is creating a key represented by a 26 lenght string where the index of the string 
represnets the frequency of letters in string. example: 

       abcdefg
abc -> 1110000000000 ....
use this as a key in hash map and time complexity will be better

"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        """
            # Not efficient O(N∗M∗Log(M))
            # N being input list and M being curr char of iteration

            anagrams = collections.defaultdict(list)
            for chars in strs: 
                sortedString = "".join(sorted(chars))
                anagrams[sortedString].append(chars)

            return anagrams.values()
        """
        
        #O(N*M)
        anagrams = collections.defaultdict(list)
        for chars in strs: 
        
            frequencies = [0] * 26 # a ... z

            for char in chars: 
                
            # ord('a') gives the ASCII value of 'a', and ord(char) gives the ASCII value of the current character.
            # Subtracting ord(char) from ord('a') gives the index of the character in the alphabet (0 for 'a', 1 for 'b', ..., 25 for 'z').
                frequencies[ord(char) - ord('a')] += 1
            
            anagrams[set(frequencies)] = chars

        return anagrams.values()