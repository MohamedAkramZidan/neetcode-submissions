class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        FirstTime = []
        for num in nums:
            if num in FirstTime:
                return True
            FirstTime.append(num)
        return False
         