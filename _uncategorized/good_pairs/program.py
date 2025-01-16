'''

# Prompt

Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.


# Constraints

1 <= nums.length <= 100
1 <= nums[i] <= 100


'''

from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        res = 0
        mapper = defaultdict(int)
        for i, num in enumerate(nums):
            res += mapper[num]
            mapper[num] += 1

        return res
