class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        reviewed_nums = {}
        for i in range(len(nums)):
            n = nums[i]
            searched_num = target - n
            if searched_num in reviewed_nums:
                return [reviewed_nums[searched_num], i]
            reviewed_nums[n] = i

