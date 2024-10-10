'''

# Prompt
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.


# Constraints

n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 1000

'''

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        for i in range(2):
            for n in nums:
                yield n


l = [1, 3, 2, 1]
s = Solution()
ans = list(s.getConcatenation(l))
print(ans)

assert ans == [1, 3, 2, 1, 1, 3, 2, 1]
