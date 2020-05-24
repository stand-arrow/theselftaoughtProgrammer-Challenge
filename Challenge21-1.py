#21-1
#21-1


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

for s in "yesterday":
    stack.push(s)

reverse = ""

while stack.size():
    reverse += stack.pop()

print reverse