'''

# Prompt

Determine if a 9 x 9 Sudoku board is valid.
Only the filled cells need to be validated according to the following rules:

    * Each row must contain the digits 1-9 without repetition.
    * Each column must contain the digits 1-9 without repetition.
    * Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    * A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    * Only the filled cells need to be validated according to the mentioned rules.


# Constraints

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.


'''

BOARD = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]


from collections import defaultdict
from typing import List


class Solution:


    def _is_valid(self, array):
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        for x in array:
            try:
                if x != '.':
                    nums.remove(x)
            except Exception as e:
                return False

        return True


    def is_valid(self, array_2d) -> bool:

        for array in array_2d:
            is_valid = self._is_valid(array)

            if not is_valid:
                return False

        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = board

        columns = [[] for _ in range(9)] * 9
        for i in range(9):
            for j in range(9):
                element = board[j][i]
                columns[i].append(element)


        count = 0
        grids = [[] for _ in range(9)] * 9
        for a in range(0, 9, 3):
            for b in range(0, 9, 3):
                for i in range(3):
                    for j in range(3):
                        element = board[i+a][j+b]

                        g = count // 9
                        grids[g].append(element)
                        count += 1

        valid_rows = self.is_valid(rows)
        valid_columns = self.is_valid(columns)
        valid_grids = self.is_valid(grids)

        return (valid_rows and valid_columns and valid_grids)


    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        columns = defaultdict(set)
        grids = defaultdict(set)

        for row in range(9):
            for column in range(9):

                element = board[row][column]
                r = row // 3
                c = column // 3
                grid = (r, c)
                if element != '.':

                    if (
                            element in rows[row] or
                            element in columns[column] or
                            element in grids[grid]
                        ):
                        return False

                    rows[row].add(element)
                    columns[column].add(element)
                    grids[grid].add(element)

        return True



solution = Solution()
answer = solution.isValidSudoku(BOARD)
assert answer

