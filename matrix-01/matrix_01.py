# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
#Example 1:
# 
# Input:
# [[0, 0, 0],
#  [0, 1, 0],
#  [0, 0, 0]]
# 
# Output:
# [[0, 0, 0],
#  [0, 1, 0],
#  [0, 0, 0]]

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if cell:
                    top = matrix[i-1][j] if i else float('inf')
                    left = matrix[i][j-1] if j else float('inf')
                    matrix[i][j] = min(top, left) +1
                        
        for i in reversed(range(rows)):
            for j in reversed(range(cols)):
                if cell := matrix[i][j]:
                    bottom = matrix[i+1][j] if i < rows-1 else float('inf')   
                    right = matrix[i][j+1] if j < cols-1 else float('inf')   
                    matrix[i][j] = min(cell, bottom+1, right+1)
        return matrix
