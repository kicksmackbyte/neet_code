'''

# Prompt

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression.
Return an integer that represents the value of the expression.

Note that:
* The valid operators are '+', '-', '*', and '/'.
* Each operand may be an integer or another expression.
* The division between two integers always truncates toward zero.
* There will not be any division by zero.
* The input represents a valid arithmetic expression in a reverse polish notation.
* The answer and all the intermediate calculations can be represented in a 32-bit integer.


# Constraints

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].


'''


from typing import List

OPERANDS = ['+', '-', '*', '/']

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operands = []

        for token in tokens:

            if token in OPERANDS:
                b = operands.pop()
                a = operands.pop()

                if token == '+':
                    result = a + b

                elif token == '-':
                    result = a - b

                elif token == '*':
                    result = a * b

                elif token == '/':
                    result = int(float(a) / b)

                operands.append(result)

            else:
                operand = int(token)
                operands.append(operand)

        return operands.pop()solution = Solution()



answer = solution.evalRPN(tokens)
assert answer == expected_answer, f'{answer} != {expected_answer}'
