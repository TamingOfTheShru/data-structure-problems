class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def make_row_zero(i, cols):
            for x in range(cols):
                matrix[i][x] = 0
            
        def make_cols_zero(rows, j):
            for x in range(rows):
                matrix[x][j] = 0
                
        temp_list = []    
        rows = len(matrix)
        cols = len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                print(i,j)
                if matrix[i][j] == 0:
                    temp_list.append([i,j])
        
        for each in temp_list:
            print(each)
            make_row_zero(each[0], cols)
            make_cols_zero(rows, each[1])
    
    
