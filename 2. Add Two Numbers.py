# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy = ListNode(0)
        result = dummy
        while l1 is not None and l2 is not None:
            num = l1.val + l2.val + carry
            carry = 0
            if num > 9:
                dummy.next = ListNode(num % 10)
                carry = 1
            else:
                dummy.next = ListNode(num)
            l1, l2, dummy = l1.next, l2.next, dummy.next
        if l1 is None and l2 is not None:
            dummy.next = self.addTwoNumbers(l2, ListNode(carry))
        if l2 is None and l1 is not None:
            dummy.next = self.addTwoNumbers(l1, ListNode(carry))
        if l1 is None and l2 is None and carry == 1:
            dummy.next = ListNode(1)
        return result.next
