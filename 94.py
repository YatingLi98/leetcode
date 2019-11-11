#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        results = []
        if not root:
            return []
        results.append(self.inorderTraversal(root.left))
        results.append([root.val])
        results.append(self.inorderTraversal(root.right))
        return results
