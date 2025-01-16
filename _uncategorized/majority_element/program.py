'''

# Prompt

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.


# Constraints

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109


'''

from collections import defaultdict


class Solution:

    def majorityElement(self, nums: List[int]) -> int:

        counter = defaultdict(int)

        for n in nums:
            counter[n] += 1

        majority = -1
        element = None

        for key, val in counter.items():
            if val > majority:
                element = key
                majority = val

        return element

