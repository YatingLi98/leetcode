# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        ans, q = [], [root]
        while q:
            ans.append([node.val for node in q])
            temp = []
            for node in q:
                temp.extend([node.left, node.right])
            q = [n for n in temp if n]
        return ans


