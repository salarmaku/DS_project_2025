class circularQueue():
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
    
    def Peek(self):
        return self.queue[self.front]