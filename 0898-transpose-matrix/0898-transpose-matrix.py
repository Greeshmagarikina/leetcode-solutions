class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        R=len(matrix)
        C=len(matrix[0])
        result=[[0]*R for _ in range (C)]
        for r in range(R):
            for c in range(C):
                result[c][r]=matrix[r][c]
        return result