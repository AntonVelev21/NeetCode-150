class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        result = []
        nums_as_dict = {}

        for num in nums:
            if num in nums_as_dict:
                nums_as_dict[num] += 1
            else:
                nums_as_dict[num] = 1

        for _ in range(k):
            most_frequent_num_k_v_pair = max(nums_as_dict.items(), key=lambda x: x[1])
            result.append(most_frequent_num_k_v_pair[0])
            nums_as_dict.pop(most_frequent_num_k_v_pair[0])

        return result

