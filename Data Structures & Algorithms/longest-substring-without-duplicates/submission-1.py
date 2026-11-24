class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep track of everything in a dict as you see it with val being index
        # if you every see an element already in dict, then rm from dict and that is the new start location and update index

        seen = {}
        start = 0
        maxlen = 0
        
        for i in range(len(s)):
            if s[i] in seen and seen[s[i]] >= start:
                
                maxlen = max(maxlen, i - start)
                while seen[s[i]] >= start:
                    start += 1
            seen[s[i]] = i
            maxlen = max(maxlen, i - start)

        return maxlen