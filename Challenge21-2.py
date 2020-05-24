#21-2

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

stack = Stack()
list = [1, 2, 3, 4, 5]

for s in list:
    stack.push(s)

reverse_list = []

while stack.size():
    reverse_list.append(stack.pop())

print(reverse_list)