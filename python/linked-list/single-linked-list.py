class Node : 
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList : 
    def __init__(self) -> None:
        self.head = None
    
    def insertNodeAtEnd(self, newNode) :
        if self.head is None :
            self.head = newNode
        else :
            lastNode = self.head
            while True :
                if lastNode.next is None:
                    break
                else :
                    lastNode = lastNode.next
            lastNode.next = newNode

    def insertNodeAtbegining(self, newNode) : 
        previousNode = self.head
        self.head = newNode
        self.head.next = previousNode

    def insertSpecificPosition(self, newNode, position) :
        currentNode = self.head
        index = 0
        while True :
            if index == position :
                previousNode.next = newNode
                newNode.next = currentNode
                break
            else :
                previousNode = currentNode
                currentNode = currentNode.next
                index = index + 1
        
    def reverseTheList(self) : 
        pre = None
        current = self.head

        while current is not None :
            next = current.next
            current.next = pre
            pre = current
            current = next
        self.head = pre
    
    def isPalindrome(self) :
        current = self.head
        count = 1
        list1 = self.head
        list2 = None
        pre = None
        while current.next is not None :
            current = current.next
            count +=1
        mid = count // 2

        while mid > 1:
            list1 = list1.next
            mid -= 1
        
        list2 = list1.next
        list1.next = None
        list1 = self.head

        while list2 is not None :
            next = list2.next
            list2.next = pre
            pre = list2
            list2 = next
        list2 = pre

        while list1 is not None :
            if list1.data != list2.data :
                return False
            else :
                list1 = list1.next
                list2 = list2.next

        return True


    def deleteNode(self, position) :
        current = self.head
        index = 0
        while True :
            if index == position :
                previous.next = current.next
                break
            else :
                previous = current
                current = current.next
                index += 1
    
    def printNodes(self) :
        nodes = self.head
        while True :
            if nodes.next is None :
                print(f"Currnet Node is : {nodes.data}")
                break
            else :
                print(f"Currnet Node is : {nodes.data}")
                nodes = nodes.next

node1 = Node("1")
linkedlist = LinkedList()
linkedlist.insertNodeAtEnd(node1)
node2 = Node("2")
linkedlist.insertNodeAtEnd(node2)
node5 = Node("3")
linkedlist.insertNodeAtEnd(node5)
node6 = Node("3")
linkedlist.insertNodeAtEnd(node6)
node3 = Node("2")
linkedlist.insertNodeAtEnd(node3)
node4 = Node("1")
linkedlist.insertNodeAtEnd(node4)
# linkedlist.insertNodeAtbegining(node3)
# node4 = Node("1")
# linkedlist.insertSpecificPosition(node4, 3)
# node4 = Node("E")
# linkedlist.insertSpecificPosition(node4, 4)
# linkedlist.deleteNode(2)
# linkedlist.reverseTheList()
res = linkedlist.isPalindrome()
print('Palindrome :', res)
# linkedlist.printNodes()