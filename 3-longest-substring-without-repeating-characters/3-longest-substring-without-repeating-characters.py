class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        maxLength = 0
        
        for r in range(len(s)):
            
            if s[r] not in seen:
                maxLength = max(maxLength,r-l+1)
                
            else:
                if seen[s[r]] < l:
                    maxLength = max(maxLength,r-l+1)
                
                else:
                    l = seen[s[r]] + 1
                
            seen[s[r]] = r
        
        return maxLength
        