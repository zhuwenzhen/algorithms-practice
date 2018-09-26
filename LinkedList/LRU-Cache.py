"""
134. LRU Cache
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache,
otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity,
it should invalidate the least recently used item before inserting a new item.

"""

class LinkedNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next #SinglyLinkedList

class LRUCache:
    """
    @:param: capacity: an integer
    """
    def __init__(self, capacity):
        self.hash = {}
        self.head = LinkedNode()
        self.tail = self.head
        self.capacity = capacity

    # like vector<LinkedNode> v; v.push_back(node)
    def push_back(self, node):
        self.hash[node.key] = self.tail # node.key : prev_node
        self.tail.next = node
        self.tail = node

    def pop_front(self):
        del self.hash[self.head.next.key] # pop out the head->next.key
        self.head.next = self.head.next.next
        self.hash[self.head.next.key] = self.head

    # kick node to the tail
    def kick(self, prev):
        node = prev.next
        if node == self.tail:
            return

        prev.next = node.next # connect so node is out
        if node.next is not None:
            self.hash[node.next.key] = prev # adjust the key to prev
            node.next = None
        self.push_back(node)

    def get(self, key): # check if key is in the hash {}
        if key not in self.hash:
            return -1
        self.kick(self.hash[key]) # adjust the sequence and update the value
        return self.hash[key].next.value

    def set(self, key, val):
        if key in self.hash:
            self.kick(self.hash[key])
            self.hash[key].next.value
        else:
            self.push_back(LinkedNode(key, val))
            if len(self.hash) > self.capacity:
                self.pop_front()

lru = LRUCache(2)
lru.set(2, 1)
lru.set(1, 1)
lru.get(2)
lru.set(4, 1)
lru.get(1)
lru.get(2)