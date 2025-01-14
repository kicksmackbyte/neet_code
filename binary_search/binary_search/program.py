'''

# Prompt

You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
Implement a function to search for target within nums.
If it exists, then return its index, otherwise, return -1.
Your solution must run in O(logn)O(logn) time.


# Constraints

1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000


'''


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        pos = len(nums) // 2
        midpoint = nums[pos]
        print(pos)

        if midpoint == target:
            return pos

        elif len(nums) == 1:
            return -1

        elif midpoint > target:
            return pos + self.search(nums[pos:], target)

        else:
            return pos + self.search(nums[0:pos], target)


    def search(self, nums: List[int], target: int) -> int:

        pos = 0
        while nums:

            index = len(nums) // 2
            midpoint = nums[index]

            if midpoint == target:
                pos += index
                return pos

            elif len(nums) == 1:
                return -1

            elif midpoint > target:
                nums = nums[0:index]

            elif midpoint < target:
                pos += index
                nums = nums[index:]

        return -1


    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1

            else:
                right = mid

        return left if (left < len(nums) and nums[left] == target) else -1


solution = Solution()

nums = [-1, 0, 2, 4, 6, 8]
answer = solution.search(nums, 3)
assert answer == -1


nums = [-1, 0, 3, 5, 9, 12]
answer = solution.search(nums, 9)
assert answer == 4, f'Expected: {4}, Got: {answer}'


nums = [2, 5]
answer = solution.search(nums, 2)
assert answer == 0, f'Expected: {0}, Got: {answer}'
