from collections import Counter
from heapq import nlargest


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        franklin = Counter(nums)
        kNums = nlargest(k, franklin, key = franklin.get)
        return kNums