'''

# Prompt

You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

1. Every open bracket is closed by the same type of close bracket.
2. Open brackets are closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.


# Constraints

1 <= s.length <= 1000

'''


mapping = {
        '(': ')',
        '{': '}',
        '[': ']',
    }

class Solution:

    def _isValid(self, s: str) -> bool:

        length = len(s)
        valid = True if length % 2 == 0 else False

        for i in range(length//2):

            open_char = s[i]
            close_char = s[length-i-1]

            if open_char not in mapping:
                valid = False
                break

            expected_char = mapping[open_char]

            if close_char != expected_char:
                valid = False
                break

        return valid


    def isValid(self, s: str) -> bool:

        length = len(s)
        valid = True if length % 2 == 0 else False

        if not valid:
            return valid


        closed_stack = []
        for i in range(length):

            char = s[i]

            if char in mapping:
                closed_char = mapping[char]
                closed_stack.append(closed_char)

            else:
                if not closed_stack:
                    valid = False
                    break

                closed_char = closed_stack.pop()

                if char != closed_char:
                    valid = False
                    break

        if closed_stack:
            valid = False

        return valid


solution = Solution()

s = '([{}])'
assert solution.isValid(s)

s = '([{})'
assert not(solution.isValid(s))


s = '()[]'
assert solution.isValid(s)


s = '()[]}{'
assert not(solution.isValid(s))


s = '(('
assert not(solution.isValid(s))
