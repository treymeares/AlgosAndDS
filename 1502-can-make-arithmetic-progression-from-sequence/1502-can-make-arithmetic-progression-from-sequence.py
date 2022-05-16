class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 2:
            return False
        srt = sorted(arr)
        difference_of_first = abs(srt[1] - srt[0])
        for x in range(1, len(arr)):
            if abs(srt[x] - srt[x-1]) != difference_of_first:
                return False
        return True
            
            
        