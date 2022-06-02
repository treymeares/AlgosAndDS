class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        prefix = 1
        for x in range(len(nums)):
            output[x] = prefix
            prefix *= nums[x]
        
        postfix = 1
        for x in range(len(nums) -1, -1, -1):
            output[x] *= postfix
            postfix *= nums[x]
        
        return output
            
