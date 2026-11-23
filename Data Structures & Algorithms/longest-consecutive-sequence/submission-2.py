class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = list(set(nums))
        numset.sort()
        count = 0
        i = 0
        while i < len(numset): 
            tmp = 0
            while i + 1 < len(numset) and numset[i] + 1 < numset[i+1]:
                i += 1
                tmp += 1
            i+=1   
            count = max(tmp, count)

        return count
             