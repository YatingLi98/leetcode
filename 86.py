# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        dummy_larger = ListNode(0)
        curr_larger = dummy_larger
        pre, curr = dummy, head
        while curr:
            while curr and curr.val < x:
                curr = curr.next
                pre = pre.next
            if not curr:
                break
            curr_larger.next = ListNode(curr.val)
            curr_larger = curr_larger.next
            pre.next = curr.next
            curr = curr.next

        while pre.next:
            pre = pre.next
        pre.next = dummy_larger.next
        return dummy.next
