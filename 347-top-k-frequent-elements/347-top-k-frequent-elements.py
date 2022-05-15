from collections import Counter
from heapq import nlargest

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ct = Counter(nums)
        k_largest = nlargest(k, ct, key=ct.get)
        return k_largest
        
        