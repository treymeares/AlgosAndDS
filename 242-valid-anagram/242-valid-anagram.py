class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        srt_s = sorted(s)
        srt_t = sorted(t)
        
        if srt_s == srt_t:
            return True
        
        return False