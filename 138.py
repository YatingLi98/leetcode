class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        if head is None:
            return head
        d = dict()
        curr = head
        while curr:
            d[curr] = Node(curr.val, None, None)
            curr = curr.next
        curr = head
        curr_copy = d[head]
        while curr:
            if curr.next:
                curr_copy.next = d[curr.next]
            if curr.random:
                curr_copy.random = d[curr.random]
            curr = curr.next
            curr_copy = curr_copy.next

        return d[head]



