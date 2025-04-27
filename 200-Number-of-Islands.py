class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                 if grid[i][j] == "1":
                    self.islands += 1
                    self.numIslandsHelper(i, j, grid)

        return self.islands

    def numIslandsHelper(self, row, col, gr):
        if col < 0 or row < 0 or col >= len(gr[0]) or row >= len(gr):
            return
        elif gr[row][col] == "0" or gr[row][col] == "x":
            return
        else:
            gr[row][col] = "x"
            self.numIslandsHelper(row + 1, col, gr)
            self.numIslandsHelper(row - 1, col, gr)
            self.numIslandsHelper(row, col + 1, gr)
            self.numIslandsHelper(row, col - 1, gr)
            return
