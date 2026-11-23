class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = list(set(nums))
        numset.sort()
        count = 0
        i = 1
        prev = numset[0]
        while i < len(numset): 
            tmp = 0
            while i < len(numset) and prev + 1 < numset[i]:
                i += 1
                tmp += 1
                prev = numset[i]
            i += 1
            count = max(tmp, count)

        return count
             