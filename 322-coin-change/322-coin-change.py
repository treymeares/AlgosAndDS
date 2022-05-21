class Solution:
    def coinChange(self, C: List[int], A: int) -> int:
        @cache
        def dp(A):
            if not A: return 0
            L = [dp(A-C[i]) for i in range(bisect.bisect(C, A)-1,-1,-1)]
            if max(L, default=-1) == -1: return -1
            return 1+min(filter(lambda x: x != -1, L))
        
        C.sort()        
        return dp(A)