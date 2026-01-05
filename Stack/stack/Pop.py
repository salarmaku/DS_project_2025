class Stack():
    def __init__(self, stack_size):
        self.size = stack_size
        self.stack = [None] * stack_size
        self.top = -1

    def isEmpty(self):
        if self.top == -1:
            return 1
        else:
            return 0
    
    def pop(self):
        if self.isEmpty == 1:
            print("This stack is already empty...")
            return None
        else:
            deleted = self.stack[self.top]
            self.stack[self.top] = None
            self.top = (self.top - 1)
            print(deleted)
            return deleted

#test
stack = Stack(5)
stack.pop()

stack.stack = [1, 2]
stack.top = 1
stack.pop()
print(stack.stack)
