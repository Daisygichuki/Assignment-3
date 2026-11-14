class Queue:
    def __init__(self, size):
        self.size = size
        self.items = []

    def enqueue(self, x):
        if len(self.items) == self.size:
            print(f"Queue Overflow: cannot insert {x}")
        else:
            self.items.append(x)             # add at the rear
            print(f"{x} enqueued")

    def dequeue(self):
        if not self.items:
            print("Queue Underflow: queue is empty")
        else:
            print(f"{self.items.pop(0)} dequeued")   # remove from the front

    def display(self):
        if self.items:
            print("Queue:", *self.items)
        else:
            print("Queue is empty")

q = Queue(3)
q.enqueue(10); q.enqueue(20); q.enqueue(30)
q.enqueue(40)       # Queue Overflow: cannot insert 40
q.dequeue()         # 10 dequeued
q.display()         # Queue: 20 30