'''

# Prompt

There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
You are given two integer array position and speed, both of length n, where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.
A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
A car fleet is a car or cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.
If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.
Return the number of car fleets that will arrive at the destination.


# Constraints

n == position.length == speed.length
1 <= n <= 105
0 < target <= 106
0 <= position[i] < target
All the values of position are unique.
0 < speed[i] <= 106


'''

from typing import List

class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # 1. Sort by postion
        cars = zip(position, speed)
        cars = sorted(cars, key=lambda car: car[0], reverse=True)

        times = []
        for position, speed in cars:

            # 2. Calculate time to target
            ttt = (target-position) / speed
            times.append(ttt)

            if len(times) >= 2 and times[-1] <= times[-2]:
                times.pop()

        # 3. see how many overlaps there are
        return len(times)


solution = Solution()

target = 12
speed = [2, 4, 1, 1, 3]
position = [10, 8, 0, 5, 3]

answer = solution.carFleet(target=target, position=position, speed=speed)
assert answer == 3, f'Got {answer}, expected 3!'


target = 10
position = [3]
speed = [3]

answer = solution.carFleet(target=target, position=position, speed=speed)
assert answer == 1, f'Got {answer}, expected 1!'


target = 100
position = [0, 2, 4]
speed = [4, 2, 1]

answer = solution.carFleet(target=target, position=position, speed=speed)
assert answer == 1, f'Got {answer}, expected 1!'
