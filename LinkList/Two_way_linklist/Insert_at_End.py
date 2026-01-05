class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None

    def insertAtEnd(self, data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
            self.end = newNode
            return

        newNode.prev = self.end
        self.end.next = newNode
        self.end = newNode
        
    def displayForward(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
        print("None")

    def displayBackward(self):
        current = self.end

        while current is not None:
            print(current.data)
            current = current.prev
        print("None")

ll = LinkedList()
ll.insertAtEnd(1)
ll.insertAtEnd(2)
ll.insertAtEnd(3)

ll.displayForward()
ll.displayBackward()

