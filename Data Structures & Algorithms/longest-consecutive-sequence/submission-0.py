class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        i = 0
        while i < len(nums): 
            tmp = 0
            while i + 1 < len(nums) and nums[i] + 1 < nums[i+1]:
                i += 1
                tmp += 1   
            count = max(tmp, count)

        return count
             