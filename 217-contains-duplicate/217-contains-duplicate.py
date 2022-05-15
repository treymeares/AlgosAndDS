class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = len(nums)
        b = len(set(nums))
        return True if b < a else False