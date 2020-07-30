"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?

   Answer: It's much simpler to set up an array version as they have pre-defined helper methods however arrays do not have a built in reference to the next element in the list.
"""


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        return self.storage.insert(0, value)

    def pop(self):
        if len(self.storage) > 0:
            return self.storage.pop(0)
        else:
            return None


class Node:
    def __init__(self, value, next_node):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail


class Stack:
    def __init__(self):
        self.size = 0
        self.value = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        new_node = Node(value, self.value.head)
        self.value.head = new_node
        self.size += 1
        if self.size == 1:
            self.value.tail = self.value.head

    def pop(self):
        if self.size > 0:
            popped = self.value.head
            self.value.head = self.value.head.next
            self.size -= 1

            if self.size == 0:
                self.value.head == None
                self.value.tail == None

            return popped.value
