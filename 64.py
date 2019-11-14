import math


class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        if not m or not n:
            return 0
        sum = [[grid[0][0] for i in range(n)] for j in range(m)]
        for i in range(1, m):
            sum[i][0] = sum[i-1][0] + grid[i][0]
        for j in range(1, n):
            sum[0][j] = sum[0][j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                sum[i][j] = min(sum[i-1][j], sum[i][j-1])+grid[i][j]
        print(sum)
        return sum[m-1][n-1]


s = Solution()

input = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

print(s.minPathSum(input))
