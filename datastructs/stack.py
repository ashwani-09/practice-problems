"""Implements Stack data structure"""

class Node:
    """Creates a single node object to store stack element"""
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Stack(Node):
    """Implementation of Stack object"""
    def __init__(self):
        self.top = None

    @property
    def isempty(self):
        """Retuns True if Stack is empty, else False"""
        return self.top is None

    @property
    def items(self):
        """Returns the elements of Stack in order from top to bottom"""
        items = []
        self.current = self.top
        while self.current is not None:
            items.append(self.current.val)
            self.current = self.current.next
        return items

    @property
    def size(self):
        """Returns the number of elements in Stack"""
        return len(self.items)

    def push(self, val):
        """Adds the element of value `val` at top"""
        node = Node(val)
        if self.isempty:
            self.top = Node(val)
        else:
            node.next = self.top
            self.top = node
        return self

    def pop(self):
        """Removes top element from Stack and returns it."""
        if self.isempty:
            return None

        item = self.top.val
        self.top = self.top.next
        return item

    def peek(self):
        """Returns the top element of Stack but doesn't remove it."""
        if self.isempty:
            return None

        return self.top.val


class StackList:
    """Implementation using Python lists"""
    def __init__(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def items(self):
        return self.items

    def size(self):
        return len(self.items)

    def push(self, val):
        self.items.append(val)
        return self

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

