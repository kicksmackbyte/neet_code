'''

# Prompt

The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2.
If there is no next greater element, then the answer for this query is -1.
Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.


# Constraints

1 <= nums1.length <= nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 104
All integers in nums1 and nums2 are unique.
All the integers of nums1 also appear in nums2.


'''

class Solution:

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        element = 0
        nums = []
        for num in nums2[::-1]:
            if num < element:
                nums.append(element)
            else:
                nums.append(-1)

            element = num

        nums = nums[::-1]

        mapper = {}
        for i, num in enumerate(nums2):
            mapper[num] = i


        answer = []
        for num in nums1:
            index = mapper[num]
            answer.append(nums[index])

        return answer



