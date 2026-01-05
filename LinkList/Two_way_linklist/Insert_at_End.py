class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtEnd(self, data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
            return

        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = newNode

    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
        print("None")

ll = LinkedList()
ll.insertAtEnd(1)
ll.insertAtEnd(2)
ll.insertAtEnd(3)

ll.display()
