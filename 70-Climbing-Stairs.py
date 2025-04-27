class Solution:
    def climbStairs(self, n: int) -> int:
        path_amounts = [1, 2]

        if n >= 3:
            for i in range(2, n):
                path_amounts.append(path_amounts[i - 1] + path_amounts[i - 2])

        return path_amounts[n - 1]
