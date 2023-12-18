# 85120485


class EmptyExpressionException(Exception):
    pass


class Stack:
    def __init__(self):
        self.__data = []

    def push(self, element):
        self.__data.append(element)

    def pop(self):
        if not self.__data:
            raise EmptyExpressionException
        return self.__data.pop()


def calc(expression):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: y - x,
        '*': lambda x, y: x * y,
        '/': lambda x, y: y // x
    }
    operands = Stack()
    for val in expression.split(' '):
        try:
            operands.push(int(val))
        except ValueError:
            operands.push(operations[val](operands.pop(), operands.pop()))

    return operands.pop()

if __name__ == '__main__':
    print(calc(input()))