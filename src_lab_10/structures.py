from collections import deque
from typing import Optional


class Stack:  
    def __init__(self):

        self._data = []

    def push(self, item) -> None:
        self._data.append(item)

    def pop(self) -> any:

        if self.is_empty():
            raise IndexError("выскакивает из пустой стопки")
        return self._data.pop()

    def peek(self) -> Optional[any]:
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self) -> bool:
        return not self._data

    def __len__(self) -> int:
        return len(self._data)


class Queue: 
    def __init__(self):
        self._data = deque()

    def enqueue(self, item) -> None:

        self._data.append(item)

    def dequeue(self) -> any:
 
        if self.is_empty():
            raise IndexError("удаление из пустой очереди")
        return self._data.popleft()

    def peek(self) -> Optional[any]:
        if self.is_empty():
            return None
        return self._data[0]

    def is_empty(self) -> bool:
        return not self._data

    def __len__(self):
        return len(self._data)