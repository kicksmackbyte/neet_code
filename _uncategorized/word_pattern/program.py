'''

# Prompt

Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
Specifically:
    * Each letter in pattern maps to exactly one unique word in s.
    * Each unique word in s maps to exactly one letter in pattern.
    * No two letters map to the same word, and no two words map to the same letter.



# Constraints

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.


'''


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        def _flatten(values):

            seen = {}
            pattern = []

            count = 0
            for value in values:
                if value not in seen:
                    seen[value] = count
                    count += 1

                pattern.append(seen[value])

            return pattern


        flattened_word = _flatten([char for char in pattern])
        flattened_sentence = _flatten(s.split(' '))

        return flattened_word == flattened_sentence
