# Definition for a binary tree node.
import collections
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    dictionary = collections.defaultdict(list)

    def helper(self, r, le, ri):
        r.left, r.right = le, ri
        return r

    def generateTrees(self, n):

        return self.generate_helper(tuple(range(1, n+1)))


    def generate_helper(self, nums):
        if len(nums) == 0:
            return [None]
        if nums in self.dictionary:
            return self.dictionary[nums]
        if len(nums) == 1:
            self.dictionary[tuple(nums)].append(TreeNode(nums[0]))
            return [TreeNode(nums[0])]
        for i in range(len(nums)):
            root = TreeNode(nums[i])
            lefts = self.generate_helper(nums[:i])
            rights = self.generate_helper(nums[i+1:])
            self.dictionary[tuple(nums)].extend([self.helper(TreeNode(root.val), left, right) for left in lefts for right in rights])
        return self.dictionary[tuple(nums)]

s = Solution()
print(s.generateTrees(3))


