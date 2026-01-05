class circularQueue():
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        if self.front == -1 and self.rear == -1:
            print("Yes")
            return 1
        else:
            print("No")
            return 0
        
queue = circularQueue(5)
queue.isEmpty()

queue.add = 2
queue.front = 0
queue.rear = 0
queue.isEmpty()
