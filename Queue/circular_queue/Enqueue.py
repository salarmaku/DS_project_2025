import Isfull
from Isempty import circularQueue as cq
class circularQueue():
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1
 
    def Enqueue(self, object):
        if Isfull.isfull():
            return False
        
        elif cq.isEmpty():
            self.front = self.rear = 0
            self.queue[self.rear] = object

        else:
            self.rear = (self.rear + 1) % self.size 
            self.queue[self.rear] = object
