class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        fill_grid = []

        if m == 1 and n == 1:
            return 1

        for i in range(0, m + 2):
            tempList = [0 for j in range(0, n + 2)]
            fill_grid.append(tempList)

        fill_grid[1][2] = 1
        fill_grid[2][1] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if i == 1 and j == 2:
                    continue
                elif i == 2 and j == 1:
                    continue

                fill_grid[i][j] += fill_grid[i - 1][j] + fill_grid[i][j- 1]

        return fill_grid[m][n]
