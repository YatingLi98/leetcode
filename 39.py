class Solution:
    def combinationSum(self, candidates, target):
        self.ans = []
        path = []
        self.candidates = candidates
        self.helper(target, 0, path)
        return self.ans

    def helper(self, target, index, path):
        if not target:
            self.ans.append(path.copy())
            return
        for i in range(index, len(self.candidates)):
            if target >= self.candidates[i]:
                path.append(self.candidates[i])
                self.helper(target - self.candidates[i], i, path)
                path.pop()


candidates = [2, 3, 6, 7]
target = 7
s = Solution()
print(s.combinationSum(candidates, target))
