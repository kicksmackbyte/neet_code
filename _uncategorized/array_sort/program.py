'''

# Prompt

Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.


# Constraints

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104


'''

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def _merge(left, right):

            res = []

            i = 0
            j = 0

            while i < len(left) and j < len(b_s):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1


            while i < len(left):
                res.append(left[i])
                i += 1

            while j < len(right):
                res.append(right[j])
                j += 1


            return res


        def _merge_sort(arr):

            m = len(arr) // 2

            left = arr[:m]
            right = arr[m:]

            print(f'm: {m}')
            print(f'arr: {arr}')
            print(f'left: {left}')
            print(f'right: {right}')
            if left or right:
                _merge_sort(left)
                _merge_sort(right)
                _merge(left, right)

        return _merge_sort(nums)


solution = Solution()
nums = [5, 2, 3, 1]
solution.sortArray(nums)
