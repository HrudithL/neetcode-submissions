class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    
        # anytime a number is added I move it up one in the list
        # this way the the indicies of the list represent the counts and the largest indicies are returned

        # or wait we can use a counter and do this same thign via that

        from collections import Counter

        counts = Counter(nums)

        # freqs = [[] * len(nums)]

        # for item in counts:
        #     count = counts[item]
        #     freqs[count].append(val)

        ans = []
        for val, count in counts.most_common():
            ans.append(val)
            if len(ans) == k:
                return ans
        return ans