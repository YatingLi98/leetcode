# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        self.inorder = inorder
        self.postorder = postorder
        self.map = {inorder[i]: i for i in range(len(inorder))}
        return self.helper(len(postorder) - 1, 0, len(inorder) - 1)

    def helper(self, post_index, instart, inend):
        if post_index < 0 or instart > inend:
            return None
        root = TreeNode(self.postorder[post_index])
        index = self.map[root.val]
        root.left = self.helper(post_index - inend + index - 1, instart, index - 1)
        root.right = self.helper(post_index - 1, index + 1, inend)
        return root


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
s = Solution()
p = s.buildTree(inorder, postorder)
