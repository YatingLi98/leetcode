import collections
import queue
class Node:
    def __init__(self, key, value, pre = None, next = None):
        self.key = key
        self.val = value
        self.pre = pre
        self.next = next

class LRUCache:

    def __init__(self, capacity):
        self.dictionary = dict()
        self.capacity = capacity
        self.head = Node(None, None)
        self.head.pre = self.head
        self.head.next = self.head

    def update(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.next = self.head.next
        node.pre = self.head
        self.head.next.pre = node
        self.head.next = node

    def get(self, key):
        if key not in self.dictionary:
            return -1
        self.update(self.dictionary[key])
        return self.dictionary[key].val

    def put(self, key, value):
        if key in self.dictionary:
            self.dictionary[key].val = value
            self.update(self.dictionary[key])
        else:
            if self.capacity == len(self.dictionary.keys()):
                self.dictionary.pop(self.head.pre.key)
                self.head.pre.pre.next = self.head
                self.head.pre = self.head.pre.pre
            node = Node(key, value)
            node.pre = self.head
            node.next = self.head.next
            self.head.next.pre = node
            self.head.next = node
            self.dictionary[key] = node



# Your LRUCache object will be instantiated and called as such:
capacity = 2
obj = LRUCache(capacity)
obj.put(2, 1)
obj.put(3, 2)
param_1 = obj.get(3)
print(param_1)
param_2 = obj.get(2)
print(param_2)
obj.put(4, 3)
param_1 = obj.get(3)
print(param_1)


