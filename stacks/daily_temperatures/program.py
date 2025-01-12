'''

# Prompt

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.


# Constraints

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100

'''

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        answers = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            for j in range(i+1, len(temperatures)):
                x = temperatures[j]

                if x > t:
                    answers[i] = j-i
                    break

        return answers


    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        length = len(temperatures)
        answers = [0] * length

        for i in range(length-2, -1, -1):
            print(f'i: {i}, t: {temperatures[i]}')
            j = i + 1

            while (j < length) and (temperatures[j] <= temperatures[i]):
                if answers[j] == 0:
                    j = length
                    break

                j += answers[j]

            if j < length:
                answers[i] = j - i


        return answers


    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        answers = []

        for t in temperatures:

            while stack:
                count = 1
                top = stack.pop()

                if t > top:
                    answers.append(count)
                    count += 1

                else:
                    stack.append(top)
                    break

            stack.append(t)
            print(stack)

        return answers




solution = Solution()

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
answer = solution.dailyTemperatures(temperatures)

print(answer)
assert answer == [1, 1, 4, 2, 1, 1, 0, 0]
