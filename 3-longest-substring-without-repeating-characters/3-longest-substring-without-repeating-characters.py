# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         result = []
#         string = ""
#         for idx, x in enumerate(s):
#             if x not in string:
#                 string += x
#             else:
#                 result.append(string)
#                 string = string[idx + 1:]
#                 string += x
#         result.append(string)
#         return len(max(result, key = len))
    
    
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_s = []
        tmp_s = ''
        for i in s:
            if i not in tmp_s:
                tmp_s += i
            else:
                max_s.append(tmp_s)
                loc = tmp_s.find(i)
                tmp_s = tmp_s[loc+1:]
                tmp_s += i

        max_s.append(tmp_s)
        
        return len(max(max_s, key=len))