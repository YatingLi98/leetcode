# Definition for singly-linked list.
import heapq


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        heap = []
        for lst in lists:
            if lst:
                heapq.heappush(heap, (lst.val, id(lst), lst))
        curr = dummy
        while heap:
            _, _, lst = heapq.heappop(heap)
            curr.next, lst = lst, lst.next
            if lst:
                heapq.heappush(heap, (lst.val, id(lst), lst))
            curr = curr.next
        return dummy.next


"""
class PriorityQueue:
    def __init__(self, args):
        self.heap = []
        for lst in args:
            if lst:
                heapq.heappush(self.heap, (lst.val, id(lst), lst))

    def pop(self):
        _, _, lst = heapq.heappop(self.heap)
        return lst

    def push(self, lst):
        if lst:
            heapq.heappush(self.heap, (lst.val, id(lst), lst))

    def is_empty(self):
        return len(self.heap) == 0


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pq = PriorityQueue(lists)
        res = []
        while not pq.is_empty():
            lst = pq.pop()
            res.append(lst.val)
            pq.push(lst.next)
        return res
"""