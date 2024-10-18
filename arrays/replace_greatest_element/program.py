'''

# Prompt

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.


# Constraints

1 <= arr.length <= 104
1 <= arr[i] <= 105


# Follow Up


'''

from typing import List


class Solution:

    def replaceElements_1(self, arr: List[int]) -> List[int]:

        length = len(arr)

        for i in range(length-1):
            num = max(arr[i+1:])
            arr[i] = num

        arr[-1] = -1

        return arr


    def replaceElements_2(self, arr: List[int]) -> List[int]:

        length = len(arr)
        new_arr = list(reversed(arr))

        ge = new_arr[0]

        for i in range(length-1):

            ge = ge if ge > new_arr[i] else new_arr[i]
            arr[i+1] = ge

        arr[0] = -1
        return list(reversed(arr))


    def replaceElements_3(self, arr: List[int]) -> List[int]:

        ge = -1
        new_arr = [-1]

        for num in arr[::-1]:

            ge = ge if ge > num else num
            new_arr.insert(0, ge)

        del new_arr[0]
        return new_arr


    def replaceElements(self, arr: List[int]) -> List[int]:

        ge = -1
        length = len(arr)

        for i, num in enumerate(arr[::-1]):
            pos = length - i - 2

            ge = ge if ge > num else num
            arr[pos] = ge

        arr[-1] = -1
        return arr


sol = Solution()
l = [17, 18, 5, 4, 6, 1]
r = [1, 6, 4, 5, 18, 17]
result = sol.replaceElements(l)

assert result == [18, 6, 6, 6, 1, -1], f'{result}'
