from dataclasses import dataclass, field


@dataclass
class MaxHeap:
    values: list[int] = field(default_factory=list)

    def __post_init__(self):
        # Avoid modifying the list passed from the caller
        self.values = self.values.copy()
        self._heapify()

    def _heapify(self):
        for index in range((len(self.values) // 2) - 1, -1, -1):
            self._sift_down(index)

    def insert(self, value: int) -> None:
        self.values.append(value)
        last_item_index = len(self.values) - 1
        self._sift_up(last_item_index)

    def _get_parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def _get_left_child_index(self, index: int) -> int:
        return (index * 2) + 1

    def _get_right_child_index(self, index: int) -> int:
        return (index * 2) + 2

    def _sift_up(self, index: int) -> None:
        if index == 0:
            return
        parent_index = self._get_parent_index(index)
        parent = self.values[parent_index]
        child = self.values[index]
        if parent >= child:
            return
        self.values[parent_index] = child
        self.values[index] = parent
        self._sift_up(parent_index)

    def _get_largest_child_index(self, parent_index: int) -> int | None:
        left_child_index = self._get_left_child_index(parent_index)
        if len(self.values) <= left_child_index:
            return None
        right_child_index = self._get_right_child_index(parent_index)
        if len(self.values) <= right_child_index:
            return left_child_index
        return max(
            left_child_index,
            right_child_index,
            key=lambda i: self.values[i],
        )

    def _sift_down(self, index: int) -> None:
        child_index = self._get_largest_child_index(index)
        if child_index is None:
            return
        if self.values[index] >= self.values[child_index]:
            return
        self.values[index], self.values[child_index] = (
            self.values[child_index],
            self.values[index],
        )
        self._sift_down(child_index)
        return

    def peek(self) -> int | None:
        if len(self.values) == 0:
            return None
        return self.values[0]

    def extract_max(self) -> int:
        if len(self.values) == 0:
            raise ValueError("There are no values in the heap.")
        max_value = self.values[0]
        if len(self.values) == 1:
            self.values.pop()
        else:
            self.values[0] = self.values.pop()
            self._sift_down(0)
        return max_value
