'''

# Prompt

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.


# Constraints


'''

class Solution:
    def hasDuplicate_1(self, nums: List[int]) -> bool:
        length = len(nums)

        for i in range(length):
            num = nums[i]

            for j in nums[i:]:
                if num == j:
                    return True

        return False


    def hasDuplicate_2(self, nums: List[int]) -> bool:
        seen = []

        for num in nums:
            if num in seen:
                return True

            seen.append(num)

        return False


    def hasDuplicate_3(self, nums: List[int]) -> bool:
        unique = set(nums)

        return len(unique) != len(nums)
