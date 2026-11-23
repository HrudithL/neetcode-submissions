class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeros = 0
        for i in nums:
            if i == 0:
                zeros += 1
            else:
                total *= i
        
        ans = []

        if zeros >= 2:
            return [0] * len(nums)
        
        for i in nums:
            ans.append(total//(i if i != 0 else 1))
        return ans