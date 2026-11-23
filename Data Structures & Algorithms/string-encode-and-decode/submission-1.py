class Solution:

    def encode(self, strs: List[str]) -> str:
        return " ".join(strs)
    def decode(self, s: str) -> List[str]:
        tmp = s.split()
        return tmp if tmp else [""]