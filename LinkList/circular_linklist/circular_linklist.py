class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def InsertAtBegin(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            new_node.next = self.head
            temp.next = new_node
            self.head = new_node

        self.size += 1

    def InsertAtEnd(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            temp.next = new_node
            new_node.next = self.head

        self.size += 1

    def InsertAtIndex(self, data, index):
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.InsertAtBegin(data)
            return

        new_node = Node(data)
        temp = self.head
        count = 0

        while count < index - 1:
            temp = temp.next
            count += 1

        new_node.next = temp.next
        temp.next = new_node
        self.size += 1

    def RemoveNodeAtBegin(self):
        if self.head is None:
            return None

        removed_data = self.head.data

        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next

            temp.next = self.head.next
            self.head = self.head.next

        self.size -= 1
        return removed_data

    def RemoveNodeAtEnd(self):
        if self.head is None:
            return None

        temp = self.head
        prev = None

        if temp.next == self.head:
            removed_data = temp.data
            self.head = None
            self.size -= 1
            return removed_data

        while temp.next != self.head:
            prev = temp
            temp = temp.next

        prev.next = self.head
        self.size -= 1
        return temp.data

    def RemoveNodeAtIndex(self, index):
        if index < 0 or index >= self.size:
            return None

        if index == 0:
            return self.RemoveNodeAtBegin()

        temp = self.head
        count = 0
        prev = None

        while count < index:
            prev = temp
            temp = temp.next
            count += 1

        prev.next = temp.next
        self.size -= 1
        return temp.data

    def SizeOfList(self):
        return self.size

# Test
cll = CircularLinkedList()

cll.InsertAtEnd(10)
cll.InsertAtEnd(20)
cll.InsertAtEnd(30)
cll.InsertAtBegin(5)

cll.RemoveNodeAtBegin()
cll.RemoveNodeAtEnd()
