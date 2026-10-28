class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Max = 0
        Set = set(nums)
        for num in Set:
            if (num -1) not in Set:
                length = 1
                while (num + length) in Set:
                    length += 1
                Max = max(length,Max)
        return Max
        