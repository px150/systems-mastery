import pytest

from arrays.delete import delete
from arrays.fixed_array import FixedArray


def test_deletes_only_element() -> None:
    array = FixedArray(
        capacity=3,
        element_size=4,
    )
    array.memory[0] = 10
    array.size = 1

    delete(array, index=0)

    assert array.memory == [None, None, None]
    assert array.size == 0


def test_deletes_last_element_without_shifting() -> None:
    array = FixedArray(
        capacity=4,
        element_size=4,
    )
    array.memory[:3] = [10, 20, 30]
    array.size = 3

    delete(array, index=2)

    assert array.memory == [10, 20, None, None]
    assert array.size == 2


def test_deletes_middle_element_by_shifting_left() -> None:
    array = FixedArray(
        capacity=5,
        element_size=4,
    )
    array.memory[:4] = [10, 20, 30, 40]
    array.size = 4

    delete(array, index=1)

    assert array.memory == [10, 30, 40, None, None]
    assert array.size == 3


def test_deletes_first_element_by_shifting_all_elements_left() -> None:
    array = FixedArray(
        capacity=4,
        element_size=4,
    )
    array.memory[:3] = [10, 20, 30]
    array.size = 3

    delete(array, index=0)

    assert array.memory == [20, 30, None, None]
    assert array.size == 2


def test_rejects_delete_from_empty_array() -> None:
    array = FixedArray(
        capacity=3,
        element_size=4,
    )

    with pytest.raises(
        ValueError,
        match="Can't delete from an empty array",
    ):
        delete(array, index=0)


@pytest.mark.parametrize("index", [-1, 3])
def test_rejects_invalid_index(index: int) -> None:
    array = FixedArray(
        capacity=4,
        element_size=4,
    )
    array.memory[:3] = [10, 20, 30]
    array.size = 3

    with pytest.raises(ValueError, match="Index out of bounds"):
        delete(array, index=index)
