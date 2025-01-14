
'''

# Prompt

Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

# Constraints

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.


'''

class Solution:

    def lengthOfLastWord(self, s: str) -> int:

        def _split(sentence):

            words = []
            word = ''

            for char in sentence:

                if char != ' ':
                    word += char

                else:
                    if word:
                        words.append(word)

                    word = ''


            if word:
                words.append(word)

            return words


        words = _split(s)
        last_word = words[-1]

        return len(last_word)


    def lengthOfLastWord(self, s: str) -> int:


        word = ''
        length = 0

        for char in s:

            if char != ' ':
                word += char

            else:
                if word:
                    length = len(word)

                word = ''


        if word:
            length = len(word)

        return length


solution = Solution()
s = "Hello World"

answer = solution.lengthOfLastWord(s)
assert answer
