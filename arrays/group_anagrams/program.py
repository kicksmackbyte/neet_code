'''

# Prompt

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.


# Constraints


1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.


'''

from collections import defaultdict
from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mapping = defaultdict(list)

        for s in strs:
            sorted_string = ''.join(sorted(s))
            mapping[sorted_string].append(s)

        return list(mapping.values())
