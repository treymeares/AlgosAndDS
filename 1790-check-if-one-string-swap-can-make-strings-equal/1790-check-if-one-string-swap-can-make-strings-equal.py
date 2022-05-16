class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        count = 0
        
        if sorted(s1) != sorted(s2):
            return False
        
        for x in range(len(s1)):
            if s1[x] == s2[x]:
                count += 1
        if count >= len(s1) - 2:
            return True
        else:
            return False
            
        
        
        