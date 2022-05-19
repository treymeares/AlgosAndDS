class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat = [num for inner in mat for num in inner]
        if len(flat) != r * c:
            return mat
        index = 0
        result = []
        for i in range(0, r):
            result.append(flat[index:index+c])
            index += c
        return result
        