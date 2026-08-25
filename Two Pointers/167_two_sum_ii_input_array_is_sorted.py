class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        nums = {}
        for i, num in enumerate(numbers):
            searched_num = target - num
            if searched_num in nums:
                return [nums[searched_num] + 1, i + 1]
            nums[num] = i

