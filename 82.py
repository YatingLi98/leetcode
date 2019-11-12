# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        curr = head
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            if pre.next == curr:
                pre.next = curr
                pre = pre.next
            else:
                pre.next = curr.next
            curr = curr.next
        return dummy.next
