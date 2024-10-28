'''

# Prompt

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.


# Constraints


2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)

'''


from typing import List


class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)
        answer = [1] * length

        prefix = 1
        for i in range(length):
            answer[i] = prefix
            prefix *= nums[i]


        postfix = 1
        for i in range(length-1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer




solution = Solution()
nums = [1, 2, 3, 4]
answer = solution.productExceptSelf(nums)

assert answer == [24, 12, 8, 6], answer
