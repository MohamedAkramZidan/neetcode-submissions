class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res,product,size = [1],1,len(nums)
        for i in range(size-1):
            product = product * nums[i]
            res.append(product)
        sufproduct = 1
        for i in range(size-1,-1,-1):
            res[i] *= sufproduct
            sufproduct *= nums[i]
        return res


        