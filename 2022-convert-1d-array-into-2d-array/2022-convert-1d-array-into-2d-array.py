class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        result = []
        start = 0
        for end in range(n, len(original) + 1, n):
            result.append(original[start:end])
            start = end
        
        return result
            
        
        