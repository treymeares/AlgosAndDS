class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        srt_s = sorted(s)
        srt_t = sorted(t)
        
        for letter in set(s):
            if s.count(letter) != t.count(letter):
                return False
        return True