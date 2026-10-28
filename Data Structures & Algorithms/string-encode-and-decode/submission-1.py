class Solution:
    def encode(self,strs: List[str]) -> str:
        if not strs:
            return ""
        res = ""
        for data in strs:
            res += str(len(data))
            res += "@"
            res += data
        return res
    def decode(self,s: str) -> list[str]:
        if not s:
            return []
        i, res = 0, []
        while i < len(s):
            j = s.find("@", i)
            length = int(s[i:j])
            i = j + 1
            res.append(s[i:i + length])
            i += length
        return res
            


