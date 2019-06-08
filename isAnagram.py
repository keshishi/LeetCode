"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""

from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        d = defaultdict(int)
            
            
        for c in s:
            d[c] += 1
        for c in t:
            d[c] -= 1
        
        for vals in d.values():
            
            if vals != 0:
                return False
        return True
