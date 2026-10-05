import pytest

from arrays.fixed_array import FixedArray
from arrays.insert import insert


def test_inserts_into_empty_array() -> None:
    array = FixedArray(
        capacity=4,
        element_size=4,
    )

    insert(array, index=0, value=10)

    assert array.memory == [10, None, None, None]
    assert array.size == 1


def test_inserts_at_end_without_shifting() -> None:
    array = FixedArray(
        capacity=4,
        element_size=4,
    )
    array.memory[:2] = [10, 20]
    array.size = 2

    insert(array, index=2, value=30)

    assert array.memory == [10, 20, 30, None]
    assert array.size == 3


def test_inserts_in_middle_by_shifting_elements_right() -> None:
    array = FixedArray(
        capacity=5,
        element_size=4,
    )
    array.memory[:4] = [10, 20, 30, 40]
    array.size = 4

    insert(array, index=1, value=15)

    assert array.memory == [10, 15, 20, 30, 40]
    assert array.size == 5


def test_inserts_at_beginning_by_shifting_all_elements_right() -> None:
    array = FixedArray(
        capacity=4,
        element_size=4,
    )
    array.memory[:3] = [10, 20, 30]
    array.size = 3

    insert(array, index=0, value=5)

    assert array.memory == [5, 10, 20, 30]
    assert array.size == 4


def test_rejects_insert_when_array_is_full() -> None:
    array = FixedArray(
        capacity=2,
        element_size=4,
    )
    array.memory[:] = [10, 20]
    array.size = 2

    with pytest.raises(ValueError, match="Array is already full"):
        insert(array, index=2, value=30)


def test_rejects_negative_index() -> None:
    array = FixedArray(
        capacity=3,
        element_size=4,
    )

    with pytest.raises(ValueError, match="Index must be non-negative"):
        insert(array, index=-1, value=10)


def test_rejects_index_greater_than_size() -> None:
    array = FixedArray(
        capacity=4,
        element_size=4,
    )
    array.memory[0] = 10
    array.size = 1

    with pytest.raises(ValueError, match="Index out of bounds"):
        insert(array, index=2, value=20)
