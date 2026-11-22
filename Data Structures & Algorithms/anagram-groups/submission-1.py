class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            tmp = str(sorted(s))
            if tmp in ans:
                ans[tmp].append(s)
            else:
                ans[tmp] = [s]
        return [ans[i] for i in ans]