class Solution:
    path = dict()
    map = None
    mm = 0
    nn = 0

    def uniquePathsWithObstacles(self, obstacleGrid):
        self.map = obstacleGrid
        self.mm = len(obstacleGrid) - 1
        self.nn = len(obstacleGrid[0]) - 1
        return self.helper(0, 0)

    def helper(self, m, n):
        if m > self.mm or n > self.nn or self.map[m][n]:
            return 0
        if m == self.mm and n == self.nn:
            return 1
        if (m, n) in self.path:
            return self.path[(m, n)]
        self.path[(m, n)] = self.helper(m+1, n) + self.helper(m , n+1)
        print(self.path)
        return self.path[(m ,n)]


s = Solution()
map = [[0, 0]]
print(s.uniquePathsWithObstacles(map))