class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stNums = set(nums)
        return len(stNums) < len(nums)
        