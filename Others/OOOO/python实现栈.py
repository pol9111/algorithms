

class Stack:
    """栈"""
    def __init__(self):
        self.__list = []

    def push(self, item):
        self.__list.append(item)

    def pop(self):
        return self.__list.pop()

    def is_empty(self):
        return not self.__list

    def peek(self):
        if self.__list:
            return self.__list[-1]

    def size(self):
        return len(self.__list)


if __name__ == '__main__':
    s = Stack()
    for i in range(8):
        s.push(i)
    print(s.is_empty())
    print(s.size())
    print(s.peek())
    print(s.pop())