class Node:
    def __init__(self, value) :
        self.data = value
        self.next = None
    

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtLast(self, newNode):
        if self.head == None:
            self.head = newNode
        else :
            current = self.head
            while current.next :
                current = current.next
            current.next = newNode

    def insertAtFirst(self, newNode) :
        newNode.next = self.head
        self.head = newNode
    def printNodes(self) :
        current = self.head
        while current :
            print(f'node : {current.data}')
            current = current.next
        



linkedlist = SinglyLinkedList()
node1 = Node('A')
linkedlist.insertAtLast(node1)
node2 = Node('B')
linkedlist.insertAtLast(node2)
node3 = Node('C')
linkedlist.insertAtLast(node3)
node4 = Node('D')
linkedlist.insertAtLast(node4)
node5 = Node('E')
linkedlist.insertAtFirst(node5)

linkedlist.printNodes()