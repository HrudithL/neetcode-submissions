class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False
        
        scounts = {}
        tcounts = {}

        for i in range(n):
            scounts[s[i]] = scounts.get(s[i], 0) + 1
            tcounts[t[i]] = tcounts.get(t[i], 0) + 1
        
        for key, val in scounts.items():
            if not key in tcounts or val != tcounts[key]:
                return False

        return True