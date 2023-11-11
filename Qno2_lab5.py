# Q no 2 implement the circular queue in python. Inculde mathoid for enqueue, 
# dequeue, checking if the queue is empty, checking
# if the queue is full, and finding the size of the queue?
class CircularQueue:
    def _init_(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.max_size == self.front

    def enqueue(self, item):
        if self.is_full():
            return "Queue is full. Cannot enqueue."

        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max_size

        self.queue[self.rear] = item
        return f"Enqueued: {item}"

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty. Cannot dequeue."

        item = self.queue[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.max_size

        return f"Dequeued: {item}"

    def size(self):
        if self.is_empty():
            return 0
        elif self.front <= self.rear:
            return self.rear - self.front + 1
        else:
            return self.max_size - self.front + self.rear + 1

CircularQueue = CircularQueue(5)
print(CircularQueue.enqueue(1))
print(CircularQueue.enqueue(2))
print(CircularQueue.enqueue(3))
print(CircularQueue.dequeue())
print(CircularQueue.enqueue(4))
print(CircularQueue.enqueue(5))
print(StopIteration.is_full())
print(StopIteration.size())