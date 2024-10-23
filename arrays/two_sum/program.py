'''

# Prompt

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.


# Constraints


2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


'''


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = [(target - n) for n in nums]

        for i, a in enumerate(new_nums):
            for j, b in enumerate(nums):
                if (a == b) and (i != j):
                    return [i, j]


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {n: i for i, n in enumerate(nums)}

        for i, n in enumerate(nums):
            val = target - n
            index = num_map.get(val, None)

            if index and index != i:
                return [index, i]
