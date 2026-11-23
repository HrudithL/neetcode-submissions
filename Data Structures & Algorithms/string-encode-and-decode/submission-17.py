class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)) + s)
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        
        decode = []
        
        i = 0
        while i < len(s):
            word = s[i: i + int(s[i]) + 1]
            decode.append(word)
            i += int(s[i])
        return decode