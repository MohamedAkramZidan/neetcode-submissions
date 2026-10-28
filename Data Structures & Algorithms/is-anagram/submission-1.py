class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        nS, nT = len(s), len(t)
        if nS != nT:
            return False
        return sorted(s) == sorted(t)
        
        