class Solution(object):
    def areAlmostEqual(self, s1, s2):
        c=0
        if sorted(s1) != sorted(s2):
            return False
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                c= c + 1
        if c >= len(s1) - 2:
            return True
        else:
            return False