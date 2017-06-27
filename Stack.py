class Stack:

    def __init__(self):
        self.arr = []

    def push(self, value):
        self.arr.append(value)

    def pop(self):
        self.arr.pop()

    def peek(self):
        return self.arr[-1]

    def is_empty(self):
        if self.arr:
            return False
        else:
            return True

    def size(self):
        return len(self.arr) - 1


if __name__ == '__main__':
    stack = Stack()
    stack.push('3')
    stack.push('4')
    stack.push('5')
    stack.size()
    stack.peek()
    stack.pop()
    stack.pop()
    print(stack.is_empty())
    stack.pop()
    print(stack.is_empty())
