class StackEmptyException(Exception):
    def __init__(self, msg="Stack está vazio."):
        self.msg = msg
        super().__init__(self.msg)


class StackFullException(Exception):
    def __init__(self, msg="Stack está cheio."):
        self.msg = msg
        super().__init__(self.msg)

class CustomStack:
    def __init__(self, pLimit):
        if pLimit <= 0:
            raise StackFullException("O limite da pilha deve ser maior que zero.")
        self.limit = pLimit
        self.elements = []

    def size(self):
        return len(self.elements)

    def isEmpty(self):
        return self.size() == 0

    def push(self, element):
        if self.size() == self.limit:
            raise StackFullException
        self.elements.append(element)

    def pop(self):
        if self.isEmpty():
            raise StackEmptyException
        return self.elements.pop()

    def top(self):
        if self.isEmpty():
            raise StackEmptyException
        return self.elements[-1]


class NumberAscOrder:
    @staticmethod
    def sort(stack):
        if stack.isEmpty():
            return []
        else:
            sorted_numbers = []
            while not stack.isEmpty():
                sorted_numbers.append(stack.pop())
            sorted_numbers.sort()
            return sorted_numbers