from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)

        l = 0
        start = 0
        minlen = float('inf')

        for r, c in enumerate(s):
            if need[c] > 0:
                missing -= 1
            
            need[c] -= 1

            while missing == 0:
                if r - l + 1 < minlen:
                    best = r - l + 1
                    start = l
                need[s[l]] += 1

                if need[s[l]] > 0:
                    missing += 1
                
                l += 1

        return s[start: start + best] if best != float('inf') else ''
