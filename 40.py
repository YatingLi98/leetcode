class Solution:
    def combinationSum2(self, candidates, target):
        self.candidates = sorted(candidates)
        self.ans = []
        path = []
        self.helper(target, 0, path)
        return self.ans

    def helper(self, target, index, path):
        if not target:
            self.ans.append(path.copy())
            return
        for i in range(index, len(self.candidates)):
            if target < self.candidates[i]:
                return
            if i > index and self.candidates[i] == self.candidates[i-1]:
                continue
            path.append(self.candidates[i])
            self.helper(target - self.candidates[i], i + 1, path)
            path.pop()


candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
s = Solution()
print(s.combinationSum2(candidates, target))
