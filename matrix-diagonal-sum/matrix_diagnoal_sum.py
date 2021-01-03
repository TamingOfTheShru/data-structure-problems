# Given a square matrix mat, return the sum of the matrix diagonals.
# 
# Only include the sum of all the elements on the primary diagonal and all the elements 
# on the secondary diagonal that are not part of the primary diagonal.

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        size = len(mat)
        diagonal_sum = 0
        for i in range(size):
            diagonal_sum += mat[i][i]
            diagonal_sum += mat[i][size-i-1]
            
        mid = size/2
        
        #if mid if float, subtract the middle value of matrix as its counted twice
        if not mid.is_integer():
            mid = size//2
            diagonal_sum = diagonal_sum - mat[mid][mid]
        return diagonal_sum
