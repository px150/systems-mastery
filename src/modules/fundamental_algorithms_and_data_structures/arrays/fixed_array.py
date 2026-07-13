from dataclasses import dataclass, field


@dataclass
class FixedArray:
    capacity: int
    element_size: int
    size: int = field(init=False)
    memory: list[int | None] = field(init=False)

    def __post_init__(self):
        if self.capacity <= 0:
            raise ValueError("Array capacity must be positive.")
        if self.element_size <= 0:
            raise ValueError("Element size must be positive.")

        self.size = 0
        self.memory = [None] * self.capacity
