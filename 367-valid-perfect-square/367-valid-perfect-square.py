class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return True
        
        left = 2
        right = num // 2
        while left <= right:
            square = (left + right) // 2
            match = square * square
            if match == num:
                return True
            elif match > num:
                right = square - 1
            else:
                left = square + 1
                
        return False
    
    