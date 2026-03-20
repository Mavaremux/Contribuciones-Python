#LIFO

class queue:
    def __init__(self):
        self.queue = []
    
    def dequeue(self, item):
        self.queue.append(item)

    def DEqueue(self):
        if self.count() == 0:
            return None
        return self.queue.pop(0)

    def count(self):
        return len(self.queue) #Desencolar haciendo pop del primer elemento
    
    def print(self):
        for item in reversed(self.queue):
              print(item)

my_queue = queue()
my_queue.dequeue("A")
my_queue.dequeue("B")
my_queue.dequeue("C")
print(my_queue.count())
my_queue.print()
my_queue.DEqueue()
print(my_queue.count())