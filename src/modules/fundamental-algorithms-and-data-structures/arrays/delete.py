from arrays.fixed_array import FixedArray


def delete(
    array: FixedArray,
    index: int,
) -> None:
    if array.size == 0:
        raise ValueError("Can't delete from an empty array.")

    if index < 0 or index >= array.size:
        raise ValueError("Index out of bounds")

    for i in range(index, array.size - 1):
        array.memory[i] = array.memory[i + 1]

    array.memory[array.size - 1] = None
    array.size -= 1
