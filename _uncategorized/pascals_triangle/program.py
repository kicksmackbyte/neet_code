'''

# Prompt

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


# Constraints

1 <= numRows <= 30


'''

class Solution:

    def generate(self, numRows: int) -> List[List[int]]:

        triangle = []

        for i in range(1, numRows+1):

            row = []
            for j in range(i):

                if (j == 0) or (j == i-1):
                    row.append(1)

                else:

                    previous_row = triangle[-1]

                    el_1 = previous_row[j-1]
                    el_2 = previous_row[j]
                    el = el_1 + el_2

                    row.append(el)

            triangle.append(row)

        return triangle

