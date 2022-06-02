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
            
# res = [1] * (len(nums))
        
#         prefix = 1
#         for i in range(len(nums)):
#             res[i] = prefix
#             prefix *= nums[i]
#         postfix = 1
#         for i in range(len(nums) - 1, -1, -1):
#             res[i] *= postfix
#             postfix *= nums[i]
#         return res