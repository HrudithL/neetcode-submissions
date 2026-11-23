class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            if sorted(s) in ans:
                ans[sorted(s)].append(s)
            else:
                ans[sorted(s)] = [s]
        return ans