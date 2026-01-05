class Stack():
    def __init__(self, stack_size):
        self.size = stack_size
        self.stack = [None] * stack_size
        self.top = -1

    def isEmpty(self):
        if self.top == -1:
            print("Yes")
            return 1
        else:
            print("no")
            return 0
#Test
stack = Stack(5)
stack.isEmpty()

stack.stack = [1]
stack.top = 0
stack.isEmpty()
