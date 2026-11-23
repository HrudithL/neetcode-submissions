class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        for i in nums:
            mult *= i
        prod = []
        for i in nums:
            if i != 0:
                prod.append(mult//i)
            else:
                prod.append(mult)
        return prod