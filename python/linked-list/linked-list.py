class Node :
    def __init__(self, data, next = None) -> None:
        self.data = data
        self.next = next

class LinkedList :
    def __init__(self) -> None:
        self.head = None

    #insert a node at the begining
    def insertAtBegining(self, data) :
        self.head = Node(data, self.head)
    
    #insert a node at the end
    def insertAtEnd(self, data) :
        newNode = Node(data)

        if self.head is None :
            self.head = newNode
        else :
            current = self.head
            while current.next :
                current = current.next
            current.next = newNode
            
    #insert at a specific position
    def insertAtSpecificPosition(self, data, position) :
        newNode = Node(data)
        current = self.head
        index = 0

        while True :
            if index == position :
                previous.next = newNode
                newNode.next = current
                break
            else :
                previous = current
                current = current.next
                index = index + 1
    
    #delete at a specific position
    def deleteAtSpecificPosition(self, position) : 
        current = self.head
        index = 0
        if self.head is None :
            print(f"Head is None")
            return
        
        while True :
            if index == position :
                previous.next = current.next
                break
            else :
                previous = current
                current = current.next
                index += 1

    #delete at the end
    def deleteAtEnd(self) :
        currentNode = self.head

        if self.head is None :
            print(f"Head is None!")
            return

        while currentNode:
            if currentNode.next is None :
                previous.next = currentNode.next
                break
            else :
                previous = currentNode
                currentNode = currentNode.next
        
            
    #print all the nodes
    def printNodes(self) :
        current = self.head

        while True :
            if current.next is None :
                print(f"Node : {current.data}")
                break
            print(f"Node : {current.data}")
            current = current.next
    
linkedlist = LinkedList()
linkedlist.insertAtEnd('C')
linkedlist.insertAtEnd('D')
linkedlist.insertAtEnd('E')
linkedlist.insertAtBegining('B')
linkedlist.insertAtBegining('A')

linkedlist.insertAtSpecificPosition('F', 3)
linkedlist.deleteAtSpecificPosition(3)
linkedlist.deleteAtEnd()

linkedlist.printNodes()
