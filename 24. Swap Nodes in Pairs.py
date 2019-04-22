# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        dummy = head
        while dummy is not None:
            if dummy.next is None:
                break
            dummy.val, dummy.next.val = dummy.next.val, dummy.val
            dummy = dummy.next.next
        return head
