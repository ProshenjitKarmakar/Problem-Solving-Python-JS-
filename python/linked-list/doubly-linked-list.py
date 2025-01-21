class Node :
    def __init__(self, data) -> None:
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList :
    def __init__(self) -> None:
        self.head = None

    def prepend(self, data) :
        new_node = Node(data)
        if self.head is None :
            self.head = new_node
            new_node.prev = None
        else :
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def append(self, data) :
        new_node = Node(data)
        if self.head is None :
            self.head = new_node
            new_node.prev = None
        else :
            current_node = self.head
            while current_node.next :
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = self.head

    

    def printNodes(self) :
        current_node = self.head
        while current_node.next : 
            print(f"Node : {current_node.data}")
            current_node = current_node.next
        print(f"Node : {current_node.data}")


dlinkedList = DoublyLinkedList()
dlinkedList.append(1)
dlinkedList.append(2)
dlinkedList.append(3)
dlinkedList.append(4)
dlinkedList.prepend(0)


dlinkedList.printNodes()
