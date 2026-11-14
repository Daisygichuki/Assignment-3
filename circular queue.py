class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.q = [None] * size
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, x):
        if self.is_full():
            print("Queue Overflow"); return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = x

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow"); return None
        x = self.q[self.front]
        if self.front == self.rear:          # last element removed
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return x

    def display(self):
        if self.is_empty():
            print("Queue is empty"); return
        i, items = self.front, []
        while True:
            items.append(self.q[i])
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print(*items)

cq = CircularQueue(5)
for v in (10, 20, 30, 40, 50):
    cq.enqueue(v)
cq.display()                       # 10 20 30 40 50
print("Dequeued:", cq.dequeue())   # 10
print("Dequeued:", cq.dequeue())   # 20
cq.enqueue(60); cq.enqueue(70)     # reuses freed slots
cq.display()                       # 30 40 50 60 70