class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSize = 0
        l = 0
        window = {}
        for right, char in enumerate(s):
            l = window[char] + 1 if char in window and window[char] >= l else l
            window[char] = right
            maxSize = max(maxSize, right - l + 1)
        return maxSize