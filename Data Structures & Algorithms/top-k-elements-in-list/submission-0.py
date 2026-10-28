class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Map = {}
        for num in nums:
            if num not in Map:
                Map[num] = 1
            Map[num] += 1
        sorted_dict = sorted(Map.items(), key=lambda item: item[1], reverse=True)
        top_k = []
        for i, item in enumerate(sorted_dict):
            if i == k:
               break 
            top_k.append(item[0])
        return top_k

        