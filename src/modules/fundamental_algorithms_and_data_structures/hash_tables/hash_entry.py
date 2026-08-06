from dataclasses import dataclass


@dataclass
class HashEntry:
    """
    Associates a key with its stored value.

    Hash tables organize lookup by hashing keys rather than values.
    Each bucket stores HashEntry objects, allowing multiple entries
    to coexist when collisions occur.
    """

    key: int
    value: int
