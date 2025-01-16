'''

# Prompt

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.


# Constraints

n == nums.length
1 <= n <= 105
1 <= nums[i] <= n


'''

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        length = len(nums)
        store = set(n for n in range(1, n+1))

        for num in nums:
            store.discard(num)

        return list(store)
