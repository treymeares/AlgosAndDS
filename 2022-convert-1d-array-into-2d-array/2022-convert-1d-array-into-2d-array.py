class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        q = []
        if m*n != len(original):
            return []
        for i in range(0, len(original), n):
            q.append(original[i:i+n])
            
        return q
            
        
        