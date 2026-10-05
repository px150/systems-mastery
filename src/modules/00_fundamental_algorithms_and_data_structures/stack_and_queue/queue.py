from dataclasses import dataclass

from arrays.dynamic_array import DynamicArray


@dataclass
class Queue:
    """
    FIFO access abstraction built on top of a DynamicArray.

    The Queue does not introduce a new memory organization.
    It constrains how the underlying collection may be accessed,
    allowing insertion at the back and removal from the front.

    Memory management remains the responsibility of DynamicArray.
    """

    _array: DynamicArray

    def enqueue(self, value: int) -> None:
        self._array.push_back(value)

    def dequeue(self) -> int:
        array_size = self._array.get_size()
        if array_size == 0:
            raise IndexError("Queue is empty.")
        return self._array.pop_front()

    def peek(self) -> int:
        array_size = self._array.get_size()
        if array_size == 0:
            raise IndexError("Queue is empty.")
        return self._array.get_item(0)
