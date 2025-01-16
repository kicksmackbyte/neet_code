from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        largest_area = 0
        for i, height in enumerate(heights):

            minimum_height = height

            area = minimum_height
            largest_area = largest_area if largest_area > area else area

            for j, next_height in enumerate(heights[i+1:], start=1):
                minimum_height = minimum_height if minimum_height < next_height else next_height
                area = (j+1)*(minimum_height)

                largest_area = largest_area if largest_area > area else area
                #print(f'j: {j}, height: {height}, next_height: {next_height}, minimum_height: {minimum_height}, area: {area}')


        return largest_area


heights = [2, 1, 5, 6, 2, 3]
expected_answer = 10

solution = Solution()
answer = solution.largestRectangleArea(heights)

assert expected_answer == answer, f'Got: {answer}, Expected: {expected_answer}'


heights = [1]
expected_answer = 1

solution = Solution()
answer = solution.largestRectangleArea(heights)

assert expected_answer == answer, f'Got: {answer}, Expected: {expected_answer}'
