class Solution:
    def longestConsecutive(self, nums):
        nums = set(nums)
        max_ = 0
        for num in nums:
            if num - 1 not in nums:
                count = 1
                while num + 1 in nums:
                    num += 1
                    count += 1
                max_ = max(max_, count)
        return max_
        