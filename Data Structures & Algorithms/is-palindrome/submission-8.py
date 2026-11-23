class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:
            if not s[left].isalpha():
                left += 1
                continue
            elif not s[right].isalpha():
                right -= 1
                continue
            
            if s[left].lower() != s[right].lower():
                return False
        return True