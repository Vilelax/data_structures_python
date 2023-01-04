class Stacks:

    def __init__(self):
        self.elements = []

    def empty(self):
        if(len(self.elements) == 0):
            return True
        return False

    def size(self):
        return len(self.elements)

    def top(self):
        if(not self.empty()):
            return self.elements[-1]

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if(not self.empty()):
            self.elements.pop()

