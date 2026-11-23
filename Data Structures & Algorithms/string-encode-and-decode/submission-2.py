class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            c = 0   
            while c < len(s):
                start = c
                while c < len(s) and s[c] == s[start]:
                    c += 1
                encoded.append(''.join([s[start], c-start-1]))
            encoded.append('_')
        
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        
        decode = []
        i = 0
        for curr in s.split('_'):
            word = []
            for i in range(0, len(curr), 2):
                word.append([curr[i]]*curr[i+1])
            decode.append(word)
        
        return ''.join(decode)