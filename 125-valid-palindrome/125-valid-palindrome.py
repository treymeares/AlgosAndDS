class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mod = ''.join(e for e in s if e.isalnum()).lower()
        left = 0
        right = len(mod) - 1
        while left <= right:
            if mod[left] != mod[right]:
                return False
            left += 1
            right -= 1
        return True