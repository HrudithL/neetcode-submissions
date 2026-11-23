class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # thinking like its basically a bunch of letters
        # we keep track of them as they move and at the end of the word we store the difference into a hashmap
        # then anytime that diff is also chosen, that is part of the list as an anagram

        
        from collections import defaultdict

        hashed = defaultdict(list)
        
        for word in strs:
            curr = [0] * 26
            for i in word:
                curr[ord(i) - ord('a')] += 1
    
            hashed[tuple(curr)].append(word)

        return hashed.values()
            