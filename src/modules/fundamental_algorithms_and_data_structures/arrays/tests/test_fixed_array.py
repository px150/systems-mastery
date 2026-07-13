import pytest

from arrays.fixed_array import FixedArray


def test_creates_empty_array_with_requested_capacity() -> None:
    array = FixedArray(
        capacity=4,
        element_size=8,
    )

    assert array.capacity == 4
    assert array.element_size == 8
    assert array.size == 0
    assert array.memory == [None, None, None, None]


def test_each_array_has_independent_memory() -> None:
    first = FixedArray(
        capacity=2,
        element_size=4,
    )
    second = FixedArray(
        capacity=2,
        element_size=4,
    )

    first.memory[0] = 10

    assert first.memory == [10, None]
    assert second.memory == [None, None]


@pytest.mark.parametrize("capacity", [0, -1])
def test_rejects_invalid_capacity(capacity: int) -> None:
    with pytest.raises(ValueError, match="Array capacity must be positive"):
        FixedArray(
            capacity=capacity,
            element_size=4,
        )


@pytest.mark.parametrize("element_size", [0, -1])
def test_rejects_invalid_element_size(element_size: int) -> None:
    with pytest.raises(ValueError, match="Element size must be positive"):
        FixedArray(
            capacity=4,
            element_size=element_size,
        )
