# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head

        # find size
        dummy = head
        size = 1
        while dummy.next:
            size += 1
            dummy = dummy.next

        k = k % size
        k = (size - k) % size - 1
        if k < 0:
            return head

        # find new head_pre
        new_head_pre = head
        while k:
            new_head_pre = new_head_pre.next
            k -= 1
        new_head = new_head_pre.next
        new_head_pre.next = None
        dummy.next = head
        return new_head


s = Solution()
first = ListNode(1)
second = ListNode(2)
first.next = second
print(s.rotateRight(first, 0))
