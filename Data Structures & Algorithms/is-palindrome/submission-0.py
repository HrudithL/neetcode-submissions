class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s)//2):
            if s[i] != s[n-i-1]:
                return false
        return true