class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(set(nums))
        nums_as_set = set(sorted_nums)
        counter = 1
        sequences = []
        for num in sorted_nums:
            searched_num = num + 1
            if searched_num in nums_as_set:
                counter += 1
            else:
                sequences.append(counter)
                counter = 1

        return max(sequences)



