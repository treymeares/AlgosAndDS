class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for idx, x in enumerate(nums):
            match = target - x
            if match in seen:
                return [idx, seen[match]]
            seen[x] = idx
        return []