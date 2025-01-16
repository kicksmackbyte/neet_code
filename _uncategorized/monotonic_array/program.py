'''

# Prompt

An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
Given an integer array nums, return true if the given array is monotonic, or false otherwise.


# Constraints

1 <= nums.length <= 105
-105 <= nums[i] <= 105


'''

class Solution:

    def isMonotonic(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        return (sorted_nums == nums) or (sorted_nums[::-1] == nums)


    def isMonotonic(self, nums: List[int]) -> bool:

        increasing = True
        decreasing = True

        last_num = nums[0]
        for num in nums:

            if (last_num > num):
                increasing = False

            if (last_num < num):
                decreasing = False

            last_num = num

        return increasing or decreasing
