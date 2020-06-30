import unittest

# 허민석 개발자님 코드 참고
_author_ = 'Minsuk Heo'


class Stack:
    def __init__(self):
        self.items = []
        self.max = 5

    def push(self, item):
        if len(self.items) < 5:
            self.items.append(item)
        else:
            print("abort push in order to prevent stack overflow")

    def pop(self):
        if len(self.items) > 0:
            self.items.pop()
        else:
            print("Stack is empty, abort pop to prevent stack underflow")

    def print_stack(self):
        print(self.items)

    def peek(self):
        return self.items[len(self.items)-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class stackTest(unittest.TestCase):
    def test(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.size(), 0)
        stack.push(1)
        stack.push(2)
        print(stack)
        stack.print_stack()
        stack.pop()
        stack.print_stack()
        stack.push(3)
        self.assertEquals(stack.peek(), 3)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.size(), 2)
        stack.pop()
        stack.pop()
        stack.pop()
        stack.push(3)
        stack.push(3)
        stack.push(3)
        stack.push(3)
        stack.push(3)
        stack.push(3)
