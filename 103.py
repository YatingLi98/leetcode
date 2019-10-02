# Definition for a binary tree node.
import queue


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def zigzagLevelOrder(self, root):
        
        if root is None:
            return
        if root.left is None and root.right is None:
            return [root.val]
        leaves = [[root.val]]
        self.layer(-1, self.take_subtree(root), leaves)
        return leaves

    def take_subtree(self, root):
        subtree = []
        if root.left is not None:
            subtree.append(root.left)
        if root.right is not None:
            subtree.append(root.right)
        return subtree

    def layer(self, is_left, roots, ans):
        if len(roots) == 0:
            return
        subroot = []
        leaves = []
        for root in roots:
            leaves.append(root.val)
            subroot.extend(self.take_subtree(root))
        if is_left == -1:
            leaves.reverse()
        ans.append(leaves)
        self.layer(-is_left, subroot, ans)


def make_tree(list):
    if list is None:
        return
    q = queue.Queue()
    root = TreeNode(list[0])
    q.put(root)
    for i in range(int(len(list) / 2)):
        curr = q.get()
        if list[2 * i + 1]:
            curr.left = TreeNode(list[2 * i + 1])
            q.put(curr.left)
        if list[2 * i + 2]:
            curr.right = TreeNode(list[2 * i + 2])
            q.put(curr.right)
    return root


lst = [3, 9, 20, None, None, 15, 7]
lst1 = [1]
root = make_tree(lst1)

s = Solution()
ans = s.zigzagLevelOrder(root)
print(ans)
