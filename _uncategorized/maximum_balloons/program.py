'''

# Prompt

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once.
Return the maximum number of instances that can be formed.


# Constraints

1 <= text.length <= 104
text consists of lower case English letters only.


'''

from collections import defaultdict


frequency = {
            'b': 1,
            'a': 1,
            'l': 2,
            'o': 2,
            'n': 1,
        }

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        counter = defaultdict(int)

        for char in text:
            if char in frequency:
                counter[char] += 1


        max_balloons = None
        for char, val in counter.items():
            f = frequency[char]
            multiples = val // f

            if multiples == 0:
                return 0
            elif max_balloons:
                max_balloons = min(max_balloons, multiples)
            else:
                max_balloons = multiples


        return max_balloons if frequency.keys() == counter.keys() else 0
