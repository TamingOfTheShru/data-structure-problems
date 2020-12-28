# Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 2:

# Input: grid = [
#  ["1","1","0","0","0"],
#  ["1","1","0","0","0"],
#  ["0","0","1","0","0"],
#  ["0","0","0","1","1"]
# ]
# Output: 3

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    Solution.markIsland(self, grid, i, j, rows, cols)
                    islands+=1
        return islands
         
    def markIsland(self, grid: List[List[str]], x: int, y: int, r:int, c:int) -> None:
        if x < 0 or x >= r or y < 0 or y >= c or grid[x][y] != "1":
            return
        grid[x][y] = "2"
        Solution.markIsland(self, grid, x+1, y, r, c)
        Solution.markIsland(self, grid, x-1, y, r, c)
        Solution.markIsland(self, grid, x, y+1, r, c)
        Solution.markIsland(self, grid, x, y-1, r, c)
        
        
