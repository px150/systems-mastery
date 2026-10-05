import pytest

from arrays.address import element_address


def test_returns_base_address_for_first_element() -> None:
    assert (
        element_address(
            base_address=1000,
            index=0,
            element_size=4,
        )
        == 1000
    )


def test_computes_address_for_later_element() -> None:
    assert (
        element_address(
            base_address=1000,
            index=3,
            element_size=4,
        )
        == 1012
    )


def test_computes_address_for_large_index() -> None:
    assert (
        element_address(
            base_address=2048,
            index=1000,
            element_size=8,
        )
        == 10048
    )


def test_addresses_are_evenly_spaced() -> None:
    base_address = 1000
    element_size = 4

    first_address = element_address(base_address, 0, element_size)
    second_address = element_address(base_address, 1, element_size)
    third_address = element_address(base_address, 2, element_size)

    assert second_address - first_address == element_size
    assert third_address - second_address == element_size


def test_rejects_negative_base_address() -> None:
    with pytest.raises(ValueError, match="Base address cannot be negative"):
        element_address(
            base_address=-1,
            index=1,
            element_size=4,
        )


def test_rejects_negative_index() -> None:
    with pytest.raises(ValueError, match="Negative index is not valid"):
        element_address(
            base_address=1000,
            index=-1,
            element_size=4,
        )


@pytest.mark.parametrize("element_size", [0, -1])
def test_rejects_invalid_element_size(element_size: int) -> None:
    with pytest.raises(ValueError, match="Element size must be positive"):
        element_address(
            base_address=1000,
            index=1,
            element_size=element_size,
        )
