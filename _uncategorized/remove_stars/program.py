'''

# Prompt

You are given a string s, which contains stars *.
In one operation, you can:
    * Choose a star in s.
    * Remove the closest non-star character to its left, as well as remove the star itself.

Return the string after all stars have been removed.
    * The input will be generated such that the operation is always possible.
    * It can be shown that the resulting string will always be unique.


# Constraints

1 <= s.length <= 105
s consists of lowercase English letters and stars *.
The operation above can be performed on s.


'''

class Solution:
    def removeStars(self, s: str) -> str:


        stack = []
        for char in s:
            if char == '*'
                stack and stack.pop()
            else:
                stack.append(c)


        return "".join(stack)
