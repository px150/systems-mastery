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
