class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            n = sum([int(i) * int(i) for i in str(n)])
            if n in seen:
                return False
            else:
                seen.add(n)
        else:
            return True