"""Implemets Queue data structure"""

class Node:
    """Creates a single node of Queue"""
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Queue(Node):
    """Implementation of Queue"""
    def __init__(self, val=None):
        if val is None:
            self.head = self.tail = None
        else:
            self.head = self.tail = Node(val)

    @property
    def isEmpty(self):
        """Checks whether Queue is empty"""
        return self.head is None

    @property
    def items(self):
        """Returns the list of items in Queue in order"""
        items = []
        self.current = self.head
        while self.current is not None:
            items.append(self.current.val)
            self.current = self.current.next

        return items

    @property
    def size(self):
        """Returns the number of elements in Queue"""
        return len(self.items)

    def enqueue(self, val):
        """Inserts element at the end of Queue"""
        if self.isEmpty:
            self.head = self.tail = Node(val)
            return self

        node = Node(val)
        self.tail.next = node
        self.tail = node
        return self

    def dequeue(self):
        """Pops the first item out of Queue"""
        if self.isEmpty:
            return None

        item = self.head.val
        self.head = self.head.next
        return item


class QueueList:
    """Implementation of Queue using Python lists object"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)