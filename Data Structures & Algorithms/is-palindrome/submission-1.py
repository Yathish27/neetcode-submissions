class Solution:
    def isPalindrome(self, s: str) -> bool:
        #check alphameric, convert to lower
        result=""
        for c in s:
            if c.isalnum():
                result+=c.lower()
        return result==result[::-1]