from queue import Queue
from tarfile import data_filter


class Queue :
    def _init_(self):
        self.data = []

    def is_empty(self):
        return not bool(self.data)

    def enqueue(self, data):
        self.data.append(data)

    def dequeue(self):
        return self.data.pop(0)

f = Queue()
f.enqueue("Premier arrivé")
f.enqueue("Deuxième arrive")
print(f.dequeue())
f.enqueue("Troisième")
while not f.is_empty():
    print(f.dequeue())

#-------------------------------------------------------
class Node :
    def _init_(self, data, next_node):
        self.data = data
        self.next_node = next_node

class Queue :
    def _init_(self):
        self_first = None
        self_last = None


    def is_empty (self):
        return self._first is None

    def enqueue (self, value):
        new_node = Node(value)
        if self._last is None:
            self._first = new_node
        else :
            self._last = new_node
        self._last = new_node

    def dequeue (self):
        if self._first is None:
            raise RuntimeError('Queue is empty')
        value = self._first.data
        self._first = self._first.next_node
        if self._first is None:
            self._last = None
        return value

f = Queue()
f.enqueue("Premier arrivé")
f.enqueue("Deuxième arrive")
print(f.dequeue())
f.enqueue("Troisième")
while not f.is_empty():
    print(f.dequeue())