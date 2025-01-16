'''

# Prompt

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).


# Constraints

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.


'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ = list(s[::-1])
        t_ = t[::-1]

        for x in t_:
            if s_ and x == s_[0]:
                s_.pop(0)

        return not(s_)


solution = Solution()
s = "abc"
t = "ahbgdc"

answer = solution.isSubsequence(s, t)
assert answer
