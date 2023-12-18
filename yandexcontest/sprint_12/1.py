# 85062792

class FullDekError(Exception):
    pass


class EmptyDekError(Exception):
    pass


class Deck:
    def __init__(self, max_length):
        self.__queue = [None] * max_length
        self.__max_n = max_length
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def _empty(self):
        return self.__size <= 0

    def _full(self):
        return self.__size >= self.__max_n

    def _count_index(self, current_index, minus=1):
        result = (current_index + 1 * minus) % self.__max_n
        return result

    def push_front(self, x):
        if self._full():
            raise FullDekError
        else:
            new_head = self._count_index(self.__head, -1)
            self.__queue[new_head] = x
            self.__size += 1
            self.__head = new_head

    def push_back(self, x):
        if self._full():
            raise FullDekError
        else:
            self.__queue[self.__tail] = x
            self.__tail = self._count_index(self.__tail)
            self.__size += 1

    def pop_front(self):
        if self._empty():
            raise EmptyDekError
        x = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = self._count_index(self.__head)
        self.__size -= 1
        return x

    def pop_back(self):
        if self._empty():
            raise EmptyDekError
        x = self.__queue[self.__tail - 1]
        self.__queue[self.__tail - 1] = None
        self.__tail = self._count_index(self.__tail, -1)
        self.__size -= 1
        return x

    def get_size(self):
        return self.__size


def read_input():
    num = int(input())
    n = int(input())
    queue = Deck(n)
    for num_command in range(num):
        command, *value = [x for x in input().strip().split()]
        try:
            a = getattr(queue, command)(*value)
            if a:
                print(a)
        except FullDekError:
            print('error')
        except EmptyDekError:
            print('error')


if __name__ == "__main__":
    read_input()
