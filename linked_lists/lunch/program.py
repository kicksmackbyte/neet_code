'''

# Prompt

The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively.
The sandwiches are placed in a stack.
All students stand in a queue.

Each student either prefers square or circular sandwiches.
The number of sandwiches in the cafeteria is equal to the number of students.

At each step:
    * If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
    * Otherwise, they will leave it and go to the queue's end.
    * This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

You are given two integer arrays
    * students and sandwiches
    * where sandwiches[i] is the type of the ith sandwich in the stack
        - (i = 0 is the top of the stack)
    * students[j] is the preference of the jth student in the initial queue
        - (j = 0 is the front of the queue).

Return the number of students that are unable to eat.


# Constraints


1 <= students.length, sandwiches.length <= 100
students.length == sandwiches.length
sandwiches[i] is 0 or 1.
students[i] is 0 or 1.


'''


from typing import List

class Solution:

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        first = True
        sandwich_eaten = False

        while (first or sandwich_eaten) and (sandwiches):

            first = False
            sandwich_eaten = False

            sandwich = sandwiches.pop(0)

            num_students = len(students)
            for j in range(num_students):
                student = students.pop(0)

                if student == sandwich:
                    sandwich_eaten = True
                    break
                else:
                    students.append(student)

        return len(students)


solution = Solution()

students = [1, 1, 1, 0, 0, 1]
sandwiches = [1, 0, 0, 0, 1, 1]

answer = solution.countStudents(students, sandwiches)
assert answer == 3, f'expected: 3, received: {answer}'
