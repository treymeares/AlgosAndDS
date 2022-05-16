class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if sorted(s1) != sorted(s2):
            return False
        
        #return true if there is no difference (strings are already equal) or there is difference of two which can be swaped
        return sum([1 if s1[i] != s2[i] else 0 for i in range(len(s1))]) in [0, 2]