class Queue:

    def __init__(self):
        self.arr = []

    def enqueue(self, value):
        self.arr = self.arr.append(value)

    def dequeue(self):
        if self.arr:
            self.arr.pop(0)

    def is_empty(self):
        if self.arr:
            return False
        else:
            return True


if __name__ == '__main__':
    queue = Queue()
    print(queue.is_empty())
    queue.enqueue('1')
    print(queue.is_empty())
    queue.dequeue()
    print(queue.is_empty())
