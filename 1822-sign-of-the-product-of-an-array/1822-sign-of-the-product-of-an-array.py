class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def signFunc(x):
            if x > 0:
                return 1
            elif x < 0:
                return -1
            else:
                return 0
        
        sign = 1
        for x in nums:
            sign *= x
        
        return signFunc(sign)
    
        