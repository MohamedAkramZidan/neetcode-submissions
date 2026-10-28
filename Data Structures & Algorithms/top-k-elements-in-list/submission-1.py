class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}
        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
        sorted_map = sorted(
            count_map.items(),
            key=lambda item: item[1],
            reverse=True
        )
        return [num for num, count in sorted_map[:k]]