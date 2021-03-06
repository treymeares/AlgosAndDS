class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left = 2
        right = x//2
        
        while left <= right:
            middle = (left + right) // 2
            num = middle * middle
            if num > x:
                right = middle - 1
            elif num < x:
                left = middle + 1
            else:
                return middle
        return right