class Queues:
    def __init__(self, size):
        self.elements = []
        self.size = size

    def enqueue(self, element):
        if(not self.isfull()):
            self.elements.append(element)

    def dequeue(self):
        if(len(self.elements) > 0 ):
            self.elements.pop(0)
            
    def peek(self):
        return self.elements[0]

    def isfull(self):
        if(len(self.elements) == self.size):
            return True
        return False

