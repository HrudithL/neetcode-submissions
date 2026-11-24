class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # count every element that we go across with window of length s1
        # then check if the counts match
        from collections import defaultdict

        if len(s1) > len(s2):
            return False

        freq1 = defaultdict(int)
        for i in s1:
            freq1[i] = freq1.get(i, 0) + 1
        
        freq2 = defaultdict(int)
        print(freq1, '_', ' ')
        for i in range(len(s1)):
            freq2[s2[i]] += 1
        print(freq2)
        for i in range(len(s1), len(s2), 1):
            if all(freq1[i] == freq2[i] for i in freq1.keys()):
                return True 
            
            freq2[s2[i]] += 1
            freq2[s2[i-len(s1)]] -= 1
            
        return all(freq1[i] == freq2[i] for i in freq1.keys())