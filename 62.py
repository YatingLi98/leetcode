class Solution:
    path = dict()
    
    def uniquePaths(self, m, n):
        if m == n == 1:
            return 1
        if m < 0 or n < 0:
            return 0
        if (m, n) in self.path:
            return self.path[(m, n)]
        self.path[(m, n)] = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        return self.path[(m, n)]
