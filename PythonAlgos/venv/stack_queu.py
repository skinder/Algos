class Helper(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class Stack(Helper):
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


class Queue(Helper):
    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items[0]



a = Stack()
print(a.isEmpty())
a.push(1)
a.push(2)
print(a.pop())
print(a.size())
print(a.isEmpty())



b = Queue()
print(b.isEmpty())
b.enqueue(3)
b.enqueue(4)
print(b.dequeue())
print(b.size())
print(b.isEmpty())