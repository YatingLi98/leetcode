class Solution:
    def permuteUnique(self, nums):
        self.ans = []
        self.nums = sorted(nums)
        path = []
        self.used = [False for i in nums]
        self.helper(0, self.used, path)
        return self.ans

    def helper(self, index, used, path):
        if index == len(self.nums):
            self.ans.append(path.copy())
            return
        for i in range(len(self.nums)):
            if used[i]:
                continue
            if i > 0 and self.nums[i] == self.nums[i-1] and used[i-1]:
                continue
            used[i] = True
            path.append(self.nums[i])
            self.helper(index+1, used, path)
            used[i] = False
            path.pop()

input = [1,1,2]
s = Solution()
print(s.permuteUnique(input))
