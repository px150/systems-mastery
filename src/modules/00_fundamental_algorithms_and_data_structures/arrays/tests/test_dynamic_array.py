import pytest

from arrays.dynamic_array import DynamicArray
from arrays.fixed_array import FixedArray


def test_push_back_adds_value_without_growing() -> None:
    dynamic_array = DynamicArray(
        array=FixedArray(
            capacity=4,
            element_size=4,
        )
    )

    dynamic_array.push_back(10)

    assert dynamic_array.array.memory == [10, None, None, None]
    assert dynamic_array.array.size == 1
    assert dynamic_array.array.capacity == 4
    assert dynamic_array.reallocation_count == 0
    assert dynamic_array.copied_elements == 0


def test_push_back_appends_after_existing_elements() -> None:
    fixed_array = FixedArray(
        capacity=4,
        element_size=4,
    )
    fixed_array.memory[:2] = [10, 20]
    fixed_array.size = 2

    dynamic_array = DynamicArray(array=fixed_array)

    dynamic_array.push_back(30)

    assert dynamic_array.array.memory == [10, 20, 30, None]
    assert dynamic_array.array.size == 3


def test_grow_doubles_capacity() -> None:
    fixed_array = FixedArray(
        capacity=2,
        element_size=4,
    )
    fixed_array.memory[:] = [10, 20]
    fixed_array.size = 2

    dynamic_array = DynamicArray(array=fixed_array)

    dynamic_array.grow()

    assert dynamic_array.array.capacity == 4
    assert dynamic_array.array.element_size == 4
    assert dynamic_array.array.memory == [10, 20, None, None]
    assert dynamic_array.array.size == 2


def test_grow_replaces_underlying_fixed_array() -> None:
    fixed_array = FixedArray(
        capacity=2,
        element_size=4,
    )
    fixed_array.memory[:] = [10, 20]
    fixed_array.size = 2

    dynamic_array = DynamicArray(array=fixed_array)

    dynamic_array.grow()

    assert dynamic_array.array is not fixed_array


def test_grow_records_reallocation_and_copied_elements() -> None:
    fixed_array = FixedArray(
        capacity=4,
        element_size=4,
    )
    fixed_array.memory[:3] = [10, 20, 30]
    fixed_array.size = 3

    dynamic_array = DynamicArray(array=fixed_array)

    dynamic_array.grow()

    assert dynamic_array.reallocation_count == 1
    assert dynamic_array.copied_elements == 3


def test_push_back_grows_when_array_is_full() -> None:
    fixed_array = FixedArray(
        capacity=2,
        element_size=4,
    )
    fixed_array.memory[:] = [10, 20]
    fixed_array.size = 2

    dynamic_array = DynamicArray(array=fixed_array)

    dynamic_array.push_back(30)

    assert dynamic_array.array.capacity == 4
    assert dynamic_array.array.memory == [10, 20, 30, None]
    assert dynamic_array.array.size == 3
    assert dynamic_array.reallocation_count == 1
    assert dynamic_array.copied_elements == 2


def test_multiple_pushes_trigger_geometric_growth() -> None:
    dynamic_array = DynamicArray(
        array=FixedArray(
            capacity=1,
            element_size=4,
        )
    )

    for value in range(8):
        dynamic_array.push_back(value)

    assert dynamic_array.array.capacity == 8
    assert dynamic_array.array.size == 8
    assert dynamic_array.array.memory == list(range(8))
    assert dynamic_array.reallocation_count == 3
    assert dynamic_array.copied_elements == 7


def test_get_size_returns_zero_for_empty_array() -> None:
    dynamic_array = DynamicArray(
        array=FixedArray(
            capacity=4,
            element_size=4,
        )
    )

    assert dynamic_array.get_size() == 0


def test_get_size_returns_number_of_stored_elements() -> None:
    fixed_array = FixedArray(
        capacity=4,
        element_size=4,
    )
    fixed_array.memory[:3] = [10, 20, 30]
    fixed_array.size = 3

    dynamic_array = DynamicArray(array=fixed_array)

    assert dynamic_array.get_size() == 3


def test_get_item_returns_value_at_index() -> None:
    fixed_array = FixedArray(
        capacity=4,
        element_size=4,
    )
    fixed_array.memory[:3] = [10, 20, 30]
    fixed_array.size = 3

    dynamic_array = DynamicArray(array=fixed_array)

    assert dynamic_array.get_item(0) == 10
    assert dynamic_array.get_item(2) == 30


def test_get_item_rejects_negative_index() -> None:
    dynamic_array = DynamicArray(
        array=FixedArray(
            capacity=4,
            element_size=4,
        )
    )

    with pytest.raises(IndexError, match="Index out of bounds."):
        dynamic_array.get_item(-1)


def test_get_item_rejects_index_equal_to_size() -> None:
    fixed_array = FixedArray(
        capacity=4,
        element_size=4,
    )
    fixed_array.memory[0] = 10
    fixed_array.size = 1

    dynamic_array = DynamicArray(array=fixed_array)

    with pytest.raises(IndexError, match="Index out of bounds."):
        dynamic_array.get_item(1)


def test_pop_back_returns_last_element() -> None:
    array = DynamicArray(
        array=FixedArray(
            capacity=2,
            element_size=4,
        )
    )

    array.push_back(10)
    array.push_back(20)

    assert array.pop_back() == 20
    assert array.get_size() == 1
    assert array.get_item(0) == 10


def test_pop_back_on_empty_array_raises_error() -> None:
    array = DynamicArray(
        array=FixedArray(
            capacity=2,
            element_size=4,
        )
    )

    with pytest.raises(IndexError, match="Array is empty."):
        array.pop_back()


def test_pop_front_returns_first_element() -> None:
    array = DynamicArray(
        array=FixedArray(
            capacity=4,
            element_size=4,
        )
    )

    array.push_back(10)
    array.push_back(20)
    array.push_back(30)

    assert array.pop_front() == 10
    assert array.get_size() == 2
    assert array.get_item(0) == 20
    assert array.get_item(1) == 30


def test_pop_front_on_empty_array_raises_error() -> None:
    array = DynamicArray(
        array=FixedArray(
            capacity=2,
            element_size=4,
        )
    )

    with pytest.raises(IndexError, match="Array is empty."):
        array.pop_front()
