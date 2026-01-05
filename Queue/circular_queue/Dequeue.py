class circularQueue():
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def isEmpty(self):
        if self.front == -1 and self.rear == -1:
            
            return True
        else:
            
            return False
        
    def Dequeue(self):
        if self.isEmpty() == True:
            print("The queue is already empty...")
            return None
        else:
            deleted = self.queue[self.front]
            self.queue[self.front] = None
            if self.front == self.rear:
                self.rear = -1
                self.front = -1
                print(deleted)
                return deleted
           
            else:
                self.front = (self.front + 1) % self.size
                print(deleted)
                return deleted
#TEST
queue = circularQueue(5)
queue.Dequeue()

queue.queue = [1, 2]
queue.rear = 1
queue.front = 0
queue.Dequeue()
print(queue.queue)
