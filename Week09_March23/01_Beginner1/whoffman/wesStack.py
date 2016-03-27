class Stack:

    def __init__(self):
        self.container = []
        self.min = None

    def push(self, item):
        self.container.append(item)
        self.min = min(self.container)

    def pop(self):
        if (self.isEmpty()):
            print("Stack is empty")
            self.min = None
        else:
            self.container.pop()
            self.min = min(self.container)

    def isEmpty(self):
        return self.size() == 0

    def getMin(self):
        return self.min

    def size(self):
        return len(self.container)
