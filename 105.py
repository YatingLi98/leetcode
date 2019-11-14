# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        self.map = {inorder[i]: i for i in range(len(inorder))}
        self.preorder = preorder
        self.inorder = inorder
        return self.helper(0, 0, len(inorder) - 1)

    def helper(self, prestart, instart, inend):
        if prestart >= len(self.preorder) or instart > inend:
            return None
        root = TreeNode(self.preorder[prestart])
        index = self.map[root.val]
        root.left = self.helper(prestart + 1, instart, index - 1)
        root.right = self.helper(prestart + index - instart + 1, index + 1, inend)
        return root


l = [0, 1, 2, 3, 0, 2, 3, 0]
print(l[1:7].index(0) + 1)
