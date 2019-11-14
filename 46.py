class Solution:
    def permute(self, nums):
        self.nums = nums
        self.ans = []
        path = []
        self.helper(0, path)
        return self.ans


    def helper(self, index, path):
        if index == len(self.nums):
            self.ans.append(path.copy())
            return
        for i in range(len(self.nums)):
            if self.nums[i] in path:
                continue
            path.append(self.nums[i])
            self.helper(index+1, path)
            path.pop()

s= Solution()
nums = [1, 2, 3]
print(s.permute(nums))