from collections import deque
class Queue :
    def __init__(self) -> None:
        self.queue = deque()

    def addToQueue(self, item) : 
        self.queue.appendleft(item)
        print(f'New Queue: {self.queue}')

    def deQueue(self) :
        deQueue = self.queue.pop()
        print(f'DeQueue element: {deQueue}')

    def is_Empty(self) :
        self.queue = deque()


queue = Queue()

queue.addToQueue(1)
queue.addToQueue(2)
queue.addToQueue(3)
queue.addToQueue(4)
queue.addToQueue(5)

queue.deQueue()
queue.deQueue()
queue.deQueue()

