# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head):
        self.lst = []

        while head:
            self.lst.append(head.val)
            head = head.next
        return self.sortLst(0, len(self.lst)-1)

    def sortLst(self, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(self.lst[start])
        mid = (start + end) // 2
        root = TreeNode(self.lst[mid])
        root.left = self.sortLst(start, mid - 1)
        root.right = self.sortLst(mid + 1, end)
        return root
