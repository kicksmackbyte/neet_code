'''

# Prompt

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".


# Constraints

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.


'''

class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = ""

        i = 0
        is_common = True

        while is_common:
            if len(strs[0]) > i:
                char = strs[0][i]
            else:
                break

            for s in strs:
                if len(s) > i and s[i] == char:
                    continue
                else:
                    is_common = False
                    break

            if is_common:
                prefix += char
                i += 1

        return prefix


    def longestCommonPrefix(self, strs: List[str]) -> str:

        for i in range(len(strs[0])):

            char = strs[0][i]

            for s in strs:
                if (len(s) == i) or (s[i] != char):
                    return s[:i]

        return strs[0]
