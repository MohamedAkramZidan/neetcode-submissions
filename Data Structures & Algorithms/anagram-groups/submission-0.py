class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Map = {}
        for word in strs:
            sWord = tuple(sorted(word))
            if sWord not in Map:
                Map[sWord] = []
            Map[sWord].append(word)
        return list(Map.values())
        

                
        