
class Stack():
    def __init__(self, stack_size):
        self.size = stack_size
        self.stack = [None] * stack_size
        self.top = -1

    def is_full(self):
        return self.top == self.size - 1
    
    def push(self, object):
        if not self.is_full():
            self.top += 1
            self.stack[self.top] = object
        else:
            print("You can't push any object, Stack is full.")