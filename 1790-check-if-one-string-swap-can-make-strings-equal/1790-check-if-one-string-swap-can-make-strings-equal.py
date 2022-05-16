class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if sorted(s1) != sorted(s2):
            return False
        difference = 0
        
        for x in range(len(s1)):
            if s1[x] != s2[x]:
                difference += 1
        if difference > 2:
            return False
        return True