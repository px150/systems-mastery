from arrays.fixed_array import FixedArray


def insert(
    array: FixedArray,
    index: int,
    value: int,
) -> None:
    """
    Insert a value into a fixed-size array by preserving contiguous memory.

    Elements after the insertion point are shifted one position to the right,
    illustrating why middle insertions require linear work.
    """
    if index < 0:
        raise ValueError("Index must be non-negative.")

    if index > array.size:
        raise ValueError("Index out of bounds.")

    if array.size == array.capacity:
        raise ValueError("Array is already full.")

    for i in range(array.size, index, -1):
        array.memory[i] = array.memory[i - 1]

    array.memory[index] = value
    array.size += 1
