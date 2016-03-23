#!/usr/bin/env python3

'''
stack.py

Author: Stefan Mendoza
Date: 22 March 2016

Implementation of the Atbash cipher.
'''

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def peek(self):
        if self._top == None:
            print("Error: Nothing in stack to return.")
            return None
        else:
            return self._top.data

    def pop(self):
        try:
            val = self._top.data
            self._top = self._top.next
            self._size = self._size - 1
        except:
            print("Error: Cannot pop empty stack.")

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.size = self.size + 1

    def size(self):
        return self._size


if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(10)
    s.push(15)
    print(s.peek())
    s.pop()
    print(s.peek())
    s.pop()
    print(s.peek())
    s.pop()
    print(s.peek())
    s.pop()
