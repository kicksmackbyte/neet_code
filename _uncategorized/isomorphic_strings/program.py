'''

# Prompt

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.


# Constraints

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.


'''

class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:

        def _flatten(string):

            seen = {}
            value = 0

            sequence = []
            for char in string:

                if char in seen:
                    sequence.append(seen[char])

                else:
                    seen[char] = value
                    sequence.append(value)
                    value += 1

            return sequence

        s_flattened = _flatten(s)
        t_flattened = _flatten(t)

        return s_flattened == t_flattened



