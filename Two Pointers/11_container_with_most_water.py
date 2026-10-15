import math


class Solution:
    def maxArea(self, heights: list[int]) -> int:
        biggest_capacity = -math.inf
        pointer_1 = 0
        pointer_2 = len(heights) - 1
        while pointer_1 < pointer_2:
            height_1 = heights[pointer_1]
            height_2 = heights[pointer_2]
            curr_cap = min(height_1, height_2) * (pointer_2 - pointer_1)
            if curr_cap > biggest_capacity:
                biggest_capacity = curr_cap

            if height_1 > height_2:
                pointer_2 -= 1

            elif height_2 > height_1:
                pointer_1 += 1

            else:
                height_1_pointer = pointer_1 + 1
                height_2_pointer = pointer_2 -1
                while height_1 == height_2:
                    if height_2_pointer <= height_1_pointer:
                        break
                    height_1, height_2 = heights[height_1_pointer], heights[height_2_pointer]
                    curr_cap = min(height_1, height_2) * (height_2_pointer - height_1_pointer)
                    if curr_cap > biggest_capacity:
                        biggest_capacity = curr_cap
                    height_1_pointer += 1
                    height_2_pointer -= 1

                if height_1 > height_2:
                    pointer_2 -= 1

                elif height_2 > height_1:
                    pointer_1 += 1

                else:
                    return biggest_capacity

        return biggest_capacity


solution = Solution().maxArea([0,1000,0,1000,0])
print(solution)

with open('data.txt', 'r') as file:
    heights = [int(x) for x in file.read().strip().split(',')]
    solution = Solution().maxArea(heights)
    print(solution)