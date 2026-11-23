class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zeros = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
            else:
                total *= nums[i]

        ans = [0] * len(nums)

        if len(zeros) >= 2:
            return ans
        elif len(zeros) == 1:
            ans[zeros[0]] = total
            return ans

        ans = []
        for i in nums:
            ans.append(total//(i if i != 0 else 1))
        return ans