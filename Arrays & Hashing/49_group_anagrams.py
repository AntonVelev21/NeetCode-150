class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = []
        while strs:
            first_word = strs[0]
            curr_anagrams = [first_word]
            for i in range(1, len(strs)):
                second_word = strs[i]
                if sorted(first_word) == sorted(second_word):
                    curr_anagrams.append(second_word)

            anagrams.append(curr_anagrams)
            for word in curr_anagrams:
                strs.remove(word)

        return anagrams


print(Solution().groupAnagrams(["act","pots","tops","cat","stop","hat"]))






