class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # thinking of k like the number of misses, we can check for a string that goes until the number of misses of k
        counts = {}
        l = 0
        maxlen = 0

        for r in range(len(s)):
            counts[s[r]] = counts.get(s[r], 0) + 1
            while (r - l + 1) - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            maxlen = max(maxlen, r - l + 1)

        return maxlen