'''

# Prompt

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.


# Constraints


0 <= nums.length <= 105
-109 <= nums[i] <= 109


'''

from typing import List
from collections import defaultdict


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0
        seen = set(nums)

        for num in seen:

            current = num
            current_longest = 0

            if (num - 1) in seen:
                continue

            while current in seen:
                current_longest += 1
                current += 1

            longest = max(longest, current_longest)

        return longest


    def longestConsecutive(self, nums: List[int]) -> int:

        results_map = defaultdict(int)
        longest = 0

        for num in nums:

            if results_map[num] == 0:

                previous_longest = results_map[num-1]
                next_longest = results_map[num+1]

                current_longest = previous_longest + next_longest + 1

                results_map[num] = current_longest
                results_map[num-previous_longest] = current_longest
                results_map[num+next_longest] = current_longest

                longest = max(longest, current_longest)

        return longest



solution = Solution()

nums = [100, 4, 200, 1, 3, 2]
answer = solution.longestConsecutive(nums)

assert answer == 4, f'{answer}'
