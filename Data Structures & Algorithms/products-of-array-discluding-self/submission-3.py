class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        for i in nums:
            total *= i
        
        ans = []
        for i in nums:
            ans.append(total/i)
        return ans