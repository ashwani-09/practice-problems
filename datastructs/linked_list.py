"""Implements Single & Double Linked Lists data stuctures
"""


class Node:
    """Creates a single node of single linked list"""
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"[{self.val}|{self.next}]"

class LinkedList(Node):
    """Implements Single Linked List Object"""

    def __init__(self, val=None):
        """Initiate list with first node"""
        if val is None:
            self.root = self.head = None
        else:
            self.root = self.head = Node(val)


    def __str__(self):
        """Print function for linked list"""
        if self.root is None:
            return "[-|None]"

        current = self.root
        output_string = ""
        while (current is not None):
            output_string = output_string + str(current.val)
            if current.next is not None:
                output_string = output_string + " ---> "

            current = current.next

        return output_string


    def __repr__(self):
        if self.root is None:
            return self.__class__.__name__ + "[]"

        else:
            current = self.root
            output_string = self.__class__.__name__ + "["
            while current is not None:
                output_string = output_string + str(current.val)
                if current.next is not None:
                    output_string = output_string + ", "
                current = current.next
            return output_string + "]"

    @property
    def items(self):
        """Prints all items of list in order"""
        if self.root is None:
            return []

        current = self.root
        items = []
        while (current is not None):
            items.append(current.val)
            current = current.next
        return items


    def add(self, val):
        """Adds a value at the end of the list"""
        if self.root is None:
            self.root = self.head = Node(val)
        else:
            node = Node(val)
            self.head.next = node
            self.head = node
            # print(f"{self.head.val} added at the end.")
        return self


    def add_at_index(self, index, val):
        """Adds a value at particular index of the list"""
        if index == 0:
            node = Node(val)
            node.next = self.root
            self.root = node
            return self

        self.current = self.root
        pos = 0
        while (pos < index - 1) & (self.current.next is not None):
            self.current = self.current.next
            pos += 1

        if (self.current is None) & (pos == index - 1):
            return self.add(val)
        elif (self.current is None):
            return self

        if pos == index - 1:
            node = Node(val)
            node.next = self.current.next
            self.current.next = node

        return self


    def search(self, val):
        """Returns the first occurence of `val`, if any, in linked list."""
        if self.root is None:
            return False

        self.current = self.root
        while (self.current.val != val) & (self.current.next is not None):
            self.current = self.current.next

        if self.current.val == val:
            return True

        return False


    def remove(self, index):
        """Removes element from index"""
        if self.root is None:
            raise IndexError("Index doesn't exist.")

        if index == 0:
            self.root = self.root.next
            return self

        self.current = self.root
        pos = 0
        while (pos < index - 1) & (self.current is not None):
            self.current = self.current.next
            pos += 1

        if pos == index - 1:
            self.current.next = self.current.next.next

        if self.current is None:
            raise IndexError("Index doesn't exist.")

        return self


class DNode:
    """Defines double linked node"""
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"[{self.left}|{self.val}|{self.right}]"

class DLinkedList(DNode):
    def __init__(self, val=None):
        if val is None:
            self.first = self.last = None
        else:
            self.first = self.last = DNode(val)

    @property
    def items(self):
        """Prints all items in list"""
        return self.forward_traverse()

    @property
    def _check_self(self):
        """Asserts the order of traversal of linked list from front & back is same."""
        if self.first is None:
            return self.last is None

        return self.forward_traverse() == self.backward_traverse()[::-1]

    def forward_traverse(self):
        """Returns list of elements as per forward traversal"""
        output = []
        self.current = self.first
        while self.current is not None:
            output.append(self.current.val)
            self.current = self.current.right
        return output

    def backward_traverse(self):
        """Returns list of elements as per backward traversal"""
        items_from_back = []
        self.current = self.last
        while self.current is not None:
            items_from_back.append(self.current.val)
            self.current = self.current.left
        return items_from_back

    def push(self, val):
        """Adds element in the beginning of linked list"""
        if self.first is None:
            self.first = self.last = DNode(val)
            return self

        node = DNode(val)
        self.first.left = node
        node.right = self.first
        self.first = node
        return self

    def append(self, val):
        """Adds element at the end of linked list"""
        if self.first is None:
            self.first = self.last = DNode(val)
            return self

        node = DNode(val)
        self.last.right = node
        node.left = self.last
        self.last = node
        return self

    def remove(self, elm):
        """Removes the first occurence of given val"""
        if self.first is None:
            raise IndexError("It's an empty list.")

        self.current = self.first
        while (self.current.right is not None) & (self.current.val != elm):
            self.current = self.current.right

        # Case 1: removing first element of list
        if (self.current.left is None) & (self.current.right is not None):
            self.first = self.current.right
            self.current = self.current.right
            self.current.left = None
            return self

        # Case 2: removing last element of list
        if (self.current.right is None) & (self.current.left is not None):
            self.current = self.current.left
            self.last = self.current
            self.current.right = None
            return self

        # Case 3: removing the only element of list
        if ((self.current.left is None)
            & (self.current.right is None)
            & (self.current.val == elm)):
            self.first = self.last = self.current = None
            return self

        # Case 4: Removing any element in between
        if ((self.current.left is not None)
            & (self.current.right is not None)
            & (self.current.val == elm)):
            self.next = self.current.right
            self.current = self.current.left
            self.current.right = self.next
            self.next.left = self.current
            return self

        raise ValueError(f"Given element {elm} not found in list.")

