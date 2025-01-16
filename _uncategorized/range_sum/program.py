'''

# Prompt

Given an integer array nums, handle multiple queries of the following type:
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).


# Constraints

1 <= nums.length <= 104
-105 <= nums[i] <= 105
0 <= left <= right < nums.length
At most 104 calls will be made to sumRange.



'''


from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.pre_computed = []

        total = 0
        for num in nums:
            total += num
            self.pre_computed.append(total)


    def _sumRange(self, left: int, right: int) -> int:

        total = 0
        for num in self.nums[left:right+1]:
            total += num

        return total


    def sumRange(self, left: int, right: int) -> int:

        right_total = self.pre_computed[right]
        left_total = self.pre_computed[left-1] if left > 0 else 0
        return right_total - left_total
