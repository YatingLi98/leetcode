# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val <= l2.val:
            result = ListNode(l1.val)
            result.next = self.mergeTwoLists(l1.next, l2)
        else:
            result = ListNode(l2.val)
            result.next = self.mergeTwoLists(l1, l2.next)
        return result
