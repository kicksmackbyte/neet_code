'''

# Prompt

You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.


# Constraints

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length


'''

class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        count = 0
        flowerbed = [0] + flowerbed + [0]

        for pos in range(1, len(flowerbed)-1):

            if (flowerbed[pos-1] == 0) and (flowerbed[pos] == 0) and (flowerbed[pos+1] == 0):
                flowerbed[pos] = 1
                count += 1

        return count >= n
