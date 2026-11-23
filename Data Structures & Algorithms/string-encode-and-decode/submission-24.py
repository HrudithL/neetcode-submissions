class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + '_' + s)
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        
        decode = []
        
        i = 0
        print(s)
        while i < len(s):
            start = i
            while s[i] != '_':
                i += 1
            length = int(s[start:i])
            word = s[i: i + length + 1]
            decode.append(word)
            i += length
        return decode