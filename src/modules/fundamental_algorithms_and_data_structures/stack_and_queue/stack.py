from dataclasses import dataclass

from arrays.dynamic_array import DynamicArray


@dataclass
class Stack:
    """
    LIFO access abstraction built on top of a DynamicArray.

    The Stack does not introduce a new memory organization.
    It constrains how the underlying collection may be accessed,
    allowing insertion and removal only at the top.

    Memory management remains the responsibility of DynamicArray.
    """

    _array: DynamicArray

    def push(self, value: int) -> None:
        self._array.push_back(value)

    def peek(self) -> int:
        array_size = self._array.get_size()
        if array_size == 0:
            raise IndexError("Stack is empty.")
        last_index = array_size - 1
        return self._array.get_item(last_index)

    def pop(self) -> int:
        array_size = self._array.get_size()
        if array_size == 0:
            raise IndexError("Stack is empty.")
        return self._array.pop_back()
