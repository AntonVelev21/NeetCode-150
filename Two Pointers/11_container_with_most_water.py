import math


class Solution:
    def maxArea(self, heights: list[int]) -> int:
        biggest_capacity = -math.inf
        pointer_1 = 0
        pointer_2 = len(heights) - 1
        while pointer_1 < pointer_2:
            height_1 = heights[pointer_1]
            height_2 = heights[pointer_2]
            curr_cap = min(height_1, height_2) * (pointer_1 - pointer_2)
            if curr_cap > biggest_capacity:
                biggest_capacity = curr_cap

            if height_1 > height_2:
                pointer_2 -= 1

            elif height_2 > height_1:
                pointer_1 += 1

            else:# Think about what should you do in the two pointers algorithm when the two heights are equal
                ...


        return biggest_capacity


with open('data.txt', 'r') as file:
    heights = [int(x) for x in file.read().strip().split(',')]
    solution = Solution().maxArea(heights)
    print(solution)