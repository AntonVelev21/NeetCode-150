import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        processed_string = ''.join([x for x in s if x in string.ascii_letters + string.digits]).lower()
        return processed_string == processed_string[-1::-1]


