class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set then count up if its the start of the sequence (meaning theres nothing bfr it in the set) unil the end, count maxes

        nset = set(nums)

        for i in nums:
            if i-1 in nset:
                continue
            else:
                count = 0
                while i+1 in nset:
                    i+=1
                    count += 1
                longest = max(count, longest)
        return longest