class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsset = set(nums)

        for i in nums:
            if target - i in numsset:
                return True
        return False