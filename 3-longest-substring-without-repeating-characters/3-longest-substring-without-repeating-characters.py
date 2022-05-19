class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = []
        string = ""
        for idx, x in enumerate(s):
            if x not in string:
                string += x
            else:
                result.append(string)
                location = string.find(x)
                string = string[location + 1:]
                string += x
        result.append(string)
        return len(max(result, key = len))