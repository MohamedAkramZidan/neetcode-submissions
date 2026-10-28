class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums)-1
        while i != j:
            two_sum = nums[i] + nums[j]
            if two_sum == target:
                return [i,j]
            elif two_sum > target:
                j -= 1
            else:
                i += 1
        return []
