# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math
class Solution:

    def isValidBST(self, root):
        return self.helper(root)

    def helper(self, root, maximum=math.inf, minimum=-math.inf):
        if not root:
            return True
        if root.val <= minimum or root.val >= maximum:
            return False
        if root.right and root.val >= root.right.val:
            return False
        if root.left and root.val <= root.left.val:
            return False
        return self.helper(root.left, root.val, minimum) and self.helper(root.right, maximum, root.val)
