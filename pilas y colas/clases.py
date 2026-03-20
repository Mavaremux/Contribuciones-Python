

#Extra

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
            self.stack.append(item)

    def pop(self):
            if not self.stack:
                return None
            return self.stack.pop()

        
    def count(self):
            return len(self.stack)
        
    def print(self):
         for item in reversed(self.stack):
              print(item)

my_stack = Stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")

print(my_stack.count())
print(my_stack.pop())
print(my_stack.count())
print(my_stack.pop())
print(my_stack.count())
