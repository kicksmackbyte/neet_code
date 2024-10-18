'''

# Prompt

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.


# Constraints


# Follow Up

Could also write a counter to keep track of how often each character is seen

'''


class Solution:

    def isAnagram(self, s: str, t: str) -> bool:

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        return sorted_s == sorted_t
