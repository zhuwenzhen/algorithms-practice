"""
494. Implement Stack by Two Queues
Implement a stack by two queues. The queue is first in first out (FIFO). That means you can not directly pop the last element in a queue.

Example
push(1)
pop()
push(2)
isEmpty() // return false
top() // return 2
pop()
isEmpty() // return true
"""
import queue
class Stack:

    def __init__(self):
        self.queue1 = queue.Queue()
        self.queue2 = queue.Queue()
    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        self.queue1.put(x)

    """
    @return: nothing
    """
    def pop(self):
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        item = self.queue1.get()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return item

    """
    @return: An integer
    """
    def top(self):
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        item = self.queue1.get()
        self.queue1, self.queue2 = self.queue2, self.queue1
        self.push(item)
        return item

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        return self.queue1.empty()