class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result = []
        if len(original) != m*n:
            return []
        for x in range(0, len(original), n):
            result.append(original[x:x+n])
        return result