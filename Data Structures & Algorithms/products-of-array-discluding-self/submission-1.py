class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        zeroes = 0
        for i in nums:
            if i == 0:
                zeroes += 1
            else:
                mult *= i

        prod = [0] * len(nums)
        if zeroes > 1:
            return prod
        

        for i in range(len(nums)):
            if zeroes:
                prod[i] = mult if nums[i] == 0 else 0
            else:
                prod[i] = mult//nums[i]
        return prod