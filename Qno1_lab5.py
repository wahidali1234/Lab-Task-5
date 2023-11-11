# Q no 1 implement a basic queue using an array in python.
# include mathods  for enqueue,dequeue,checking checking 
#  in the queue is empty,and finding the size of the queue in python?
class Queue:
    def _init_(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Cannot dequeue from an empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print("Queue:", my_queue.items)
print("Dequeue:", my_queue.dequeue())
print("Queue after dequeue:", my_queue.items)
print("Is empty?", my_queue.is_empty())
print("Queue size:", my_queue.size())