'''

# Prompt

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


# Constraints

1 <= n <= 8


'''

from typing import List

class Solution:
    def _generateParenthesis(self, n: int) -> List[str]:

        solutions = ['']

        for i in range(n):
            for _ in range(len(solutions)):
                element = solutions.pop(0)

                solution = f'(){element}'
                if solution not in solutions:
                    solutions.append(solution)

                solution = f'{element}()'
                if solution not in solutions:
                    solutions.append(solution)

                solution = f'({element})'
                if solution not in solutions:
                    solutions.append(solution)


        return solutions


    def generateParenthesis(self, n: int) -> List[str]:

        solutions = []
        stack = []

        def backtrack(open_count, closed_count):

            if (open_count == closed_count) and (open_count == n):

                solution = ''.join(stack)
                solutions.append(solution)

                return solutions

            if open_count < n:
                stack.append('(')
                backtrack(open_count+1, closed_count)
                stack.pop()

            if closed_count < open_count:
                stack.append(')')
                backtrack(open_count, closed_count+1)
                stack.pop()

        backtrack(0, 0)
        return solutions


solution = Solution()

answer = solution.generateParenthesis(3)
expected_answer = ["()()()", "(()())","()(())","(())()", "((()))"]

assert answer == expected_answer
