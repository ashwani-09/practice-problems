import unittest
from linked_list import LinkedList, DLinkedList
from queue import Queue
from stack import Stack

class TestStack(unittest.TestCase):
    def test_setup(self):
        self.assertTrue(Stack().isempty)
        self.assertEqual(Stack().size, 0)

    def test_push(self):
        self.assertEqual(Stack().push(0).items, [0])
        self.assertEqual(Stack().push(0).push(1).items, [1, 0])

    def test_pop(self):
        self.assertEqual(Stack().pop(), None)

        stack = Stack()
        self.assertEqual(stack.push(0).pop(), 0)
        self.assertEqual(stack.size, 0)
        self.assertEqual(stack.push(0).push(1).push(2).pop(), 2)
        self.assertEqual(stack.size, 2)

    def test_peek(self):
        self.assertEqual(Stack().peek(), None)

        stack = Stack()
        self.assertEqual(stack.push(0).peek(), 0)
        self.assertEqual(stack.size, 1)
        self.assertEqual(stack.push(0).push(1).push(2).peek(), 2)
        self.assertEqual(stack.size, 4)


class TestQueue(unittest.TestCase):
    def test_setup(self):
        self.assertTrue(Queue().isEmpty)
        self.assertFalse(Queue(1).isEmpty)
        self.assertEqual(Queue().size, 0)
        self.assertEqual(Queue(0).size, 1)

    def test_enqueue(self):
        self.assertEqual(Queue().enqueue(0).items, [0])
        self.assertEqual(Queue(0).enqueue(1).items, [0, 1])

    def test_dequeue(self):
        self.assertEqual(Queue().dequeue(), None)

        q = Queue()
        self.assertEqual(q.enqueue(0).dequeue(), 0)
        self.assertEqual(q.size, 0)

        q = Queue()
        self.assertEqual(q.enqueue(0).enqueue(1).dequeue(), 0)
        self.assertEqual(q.items, [1])


class TestDoubleLinkedList(unittest.TestCase):
    def test_setup(self):
        self.assertEqual(DLinkedList().items, [])
        self.assertEqual(DLinkedList(0).items, [0])

    def test_push(self):
        self.assertEqual(DLinkedList().push(0).items, [0])
        self.assertEqual(DLinkedList().push(1).push(0).items, [0, 1])
        self.assertTrue(DLinkedList().push(1).push(0)._check_self)

    def test_append(self):
        self.assertEqual(DLinkedList().append(0).items, [0])
        self.assertEqual(DLinkedList(0).append(1).items, [0, 1])
        self.assertTrue(DLinkedList().append(0).append(1)._check_self)

    def test_remove(self):
        self.assertEqual(DLinkedList().append(0).append(1).remove(0).items, [1])
        self.assertTrue(DLinkedList().append(0).append(1).remove(0)._check_self)
        self.assertEqual(DLinkedList().append(0).append(1).remove(1).items, [0])
        self.assertTrue(DLinkedList().append(0).append(1).remove(1)._check_self)
        self.assertEqual(DLinkedList().append(0).append(1).append(2).remove(1).items, [0, 2])
        self.assertTrue(DLinkedList().append(0).append(1).append(2).remove(1)._check_self)
        self.assertEqual(DLinkedList().append(0).remove(0).items, [])
        self.assertTrue(DLinkedList().append(0).remove(0)._check_self)

        with self.assertRaises(IndexError):
            DLinkedList().remove(0)

        with self.assertRaises(ValueError):
            DLinkedList(1).remove(0)


class TestLinkedList(unittest.TestCase):
    def test_setup(self):
        self.assertEqual(LinkedList().items, [])
        self.assertEqual(LinkedList(0).items, [0])

    def test_add(self):
        ll = LinkedList()
        self.assertEqual(ll.add(1).items, [1])
        self.assertEqual(ll.add(2).add(3).items, [1, 2, 3])
        self.assertEqual(ll.add_at_index(0, 0).items, [0, 1, 2, 3])
        self.assertEqual(ll.add_at_index(3, 4).items, [0, 1, 2, 4, 3])
        self.assertEqual(LinkedList().add_at_index(0, 0).items, [0])

    def test_search(self):
        self.assertTrue(LinkedList(0).search(0), "First element in [0]")
        self.assertTrue(LinkedList().add(0).add(1).search(1), "Last element in [0, 1]")
        self.assertTrue(LinkedList().add(0).add(1).add(2).search(1), "Middle element in [0, 1, 2]")
        self.assertFalse(LinkedList().search(0), "Empty list.")
        self.assertFalse(LinkedList(0).search(1), "1 doesn't exist in [0]")

    def test_remove(self):
        self.assertEqual(LinkedList().add(2).remove(0).items, [])
        self.assertEqual(LinkedList().add(0).add(1).add(2).add(3).remove(2).items, [0, 1, 3])
        self.assertEqual(LinkedList().add(0).add(1).remove(1).items, [0])


if __name__ == '__main__':
    unittest.main()

