class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
	def __init__(self):
		self.top = None
		self.size = 0
	
	def push(self, value):
		node = Node(value)
		node.next = self.top
		self.top = node
		self.size += 1

	def pop(self):
		value = self.top.value
		self.top = self.top.next
		self.size -= 1
		return value

	def size(self):
		return self.size

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
stack.push(4)
print(stack.pop())
print(stack.pop())