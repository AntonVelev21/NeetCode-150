class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triples = []
        sorted_nums = sorted(nums)
        checked_nums = set()

        for i, num1 in enumerate(sorted_nums):
            if num1 not in checked_nums:
                checked_nums.add(num1)
                target_num = -num1
                pointer_1 = i + 1
                pointer_2 = len(sorted_nums) - 1
                curr_iteration_numbers = set()
                while pointer_2 > pointer_1:
                    if target_num > sorted_nums[pointer_1] + sorted_nums[pointer_2]:
                        pointer_1 += 1

                    elif target_num < sorted_nums[pointer_1] + sorted_nums[pointer_2]:
                        pointer_2 -= 1

                    else:
                        if sorted_nums[pointer_1] not in curr_iteration_numbers and sorted_nums[pointer_2] not in curr_iteration_numbers:
                            triples.append([num1, sorted_nums[pointer_1], sorted_nums[pointer_2]])
                            curr_iteration_numbers.add(sorted_nums[pointer_1])
                            curr_iteration_numbers.add(sorted_nums[pointer_2])
                        pointer_1 += 1
                        pointer_2 -= 1

        return triples
