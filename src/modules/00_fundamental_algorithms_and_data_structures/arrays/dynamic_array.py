from dataclasses import dataclass

from .fixed_array import FixedArray


@dataclass
class DynamicArray:
    array: FixedArray
    reallocation_count: int = 0
    copied_elements: int = 0

    def push_back(self, value: int) -> None:
        if self.array.size == self.array.capacity:
            self.grow()
        self.array.memory[self.array.size] = value
        self.array.size += 1

    def grow(self) -> None:
        """
        Allocate a larger contiguous block and copy all existing elements.

        Dynamic arrays do not expand in place.
        They replace their underlying contiguous storage with a larger one.
        This illustrates why growing a dynamic array is an O(n) operation.
        """
        old_array = self.array
        self.array = FixedArray(
            capacity=old_array.capacity * 2,
            element_size=old_array.element_size,
        )
        for i in range(old_array.size):
            self.array.memory[i] = old_array.memory[i]
            self.copied_elements += 1
        self.array.size = old_array.size
        self.reallocation_count += 1

    def get_size(self) -> int:
        return self.array.size

    def get_item(self, index: int) -> int:
        if index < 0 or index >= self.array.size:
            raise IndexError("Index out of bounds.")
        return self.array.memory[index]

    def pop_back(self) -> int:
        """
        Remove and return the last element of the dynamic array.

        Removing the final element preserves the contiguous memory layout
        without shifting any remaining elements, making this an O(1) operation.

        Raises:
            IndexError: If the array is empty.
        """
        if self.array.size == 0:
            raise IndexError("Array is empty.")
        last_index = self.array.size - 1
        last_item = self.array.memory[last_index]
        self.array.memory[last_index] = None
        self.array.size -= 1
        return last_item

    def pop_front(self) -> int:
        """
        Remove and return the first element of the dynamic array.

        Removing the first element requires shifting all remaining
        elements one position toward the beginning of the array in
        order to preserve contiguous memory.

        This illustrates why removing from the front of a contiguous
        array is an O(n) operation.

        Raises:
            IndexError: If the array is empty.
        """
        if self.array.size == 0:
            raise IndexError("Array is empty.")
        first_item = self.array.memory[0]
        for i in range(self.array.size):
            is_last_index = i == self.array.size - 1
            if is_last_index:
                self.array.memory[i] = None
                break
            self.array.memory[i] = self.array.memory[i + 1]
        self.array.size -= 1
        return first_item
