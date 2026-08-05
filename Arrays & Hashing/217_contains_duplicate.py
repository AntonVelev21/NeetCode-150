class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        reviews_nums = {}
        for n in nums:
            if n in reviews_nums:
                return True
            reviews_nums[n] = True

        return False





