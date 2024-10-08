'''
# Prompt

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
The remaining elements of nums are not important as well as the size of nums.
Return k.


# Constraints

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.

'''

from typing import List


class Solution:
    def _removeDuplicates(self, nums: List[int]) -> int:
        new_nums = []

        for num in nums:
            if num not in new_nums:
                new_nums.append(num)

        k = len(new_nums)
        for i in range(k):
            nums[i] = new_nums[i]

        return k


    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        current = None

        for num in nums:
            if current != num:
                nums[k] = num
                k += 1

                current = num

        return k



l = [1,1,2]
s = Solution()
s.removeDuplicates(l)
print(l)
