#21 Stack

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
#for i in range(0, 6):
#   stack.push(i)

#print(stack.peek())
#print(item)
#print(stack.is_empty())
#print(stack.size())

#reverse
for c in "Hello":
    stack.push(c)

reverse = ""

while stack.size():
    reverse += stack.pop()

print(reverse)