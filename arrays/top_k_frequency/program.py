'''

# Prompt

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.


# Constraints

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.



'''


from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

        sorted_nums = sorted(counter.keys(), key=lambda k: counter[k], reverse=True)
        return sorted_nums[:k]
