class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        max_ = 0
        current = []
        if len(s) == 1:
            return 1
        while right < len(s):
            current = s[left:right]
            if s[right] not in current:
                right += 1
            else:
                left += 1
            current = s[left:right]
            max_ = max(len(current), max_)
            print (current)
        return max_