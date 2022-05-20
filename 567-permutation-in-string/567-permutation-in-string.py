class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dct = collections.defaultdict(int)
        comp = collections.Counter(s1)
        
        l = 0
        
        for r, ch in enumerate(s2):
            dct[ch] += 1
            
            if r - l + 1 == len(s1):
                if dct == comp: 
                    return True
                dct[s2[l]] -= 1
                
                if dct[s2[l]] == 0:
                    del dct[s2[l]]
                
                l += 1
        
        return False