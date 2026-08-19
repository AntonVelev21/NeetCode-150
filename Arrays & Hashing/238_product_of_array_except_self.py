class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = []
        prefix = []
        suffix = []

        for i in range(len(nums)):
            if i == 0:
                curr_prefix = 1
            else:
                curr_prefix = nums[i - 1] * prefix[-1]
            prefix.append(curr_prefix)

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                curr_sufix = 1
            else:
                curr_sufix = nums[i + 1] * suffix[-1]

            suffix.append(curr_sufix)

        index = len(suffix) - 1
        for i in range(len(nums)):
            product = prefix[i] * suffix[index]
            index -= 1
            output.append(product)
        return output


