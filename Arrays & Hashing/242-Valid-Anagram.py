class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        for c in s:
            if c not in dict_s:
                dict_s[c] = 1
            else:
                dict_s[c] += 1

        for c in t:
            if c not in dict_s:
                return False
            dict_s[c] -= 1
            if dict_s[c]  == 0:
                dict_s.pop(c)

        if len (dict_s) == 0:
            return True

        return False
