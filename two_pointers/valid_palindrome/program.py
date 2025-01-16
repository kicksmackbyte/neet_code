'''

# Prompt

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.


# Constraints

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.


'''


class Solution:

    def _alphaNum(self, c):

        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


    def isPalindrome(self, s: str) -> bool:

        l = 0
        r = len(s) - 1
        while l < r:

            while l < r and not(self._alphaNum(s[l])):
                l += 1

            while l < r and not(self._alphaNum(s[r])):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True


solution = Solution()

s = 'racecar'
answer = solution.isPalindrome(s)

assert answer


s = 'racecaR'
answer = solution.isPalindrome(s)

assert answer

s = "A man, a plan, a canal: Panama"
answer = solution.isPalindrome(s)
assert answer


s = "A an, a plan, a canal: Panama"
answer = solution.isPalindrome(s)
assert not(answer)
