def element_address(base_address: int, index: int, element_size: int) -> int:
    """
    Computes the physical memory address of an array element.

    This demonstrates that array indexing is an address calculation
    rather than a search operation.
    """
    if base_address < 0:
        raise ValueError("Base address cannot be negative")

    if index < 0:
        raise ValueError("Negative index is not valid")

    if element_size <= 0:
        raise ValueError("Element size must be positive")

    return base_address + (index * element_size)
