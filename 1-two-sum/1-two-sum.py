class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for idx, number in enumerate(nums):
            match = target - number
            if match in seen:
                return [idx, seen[match]]
            seen[number] = idx
        return []
        