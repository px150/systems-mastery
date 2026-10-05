def linear_search(values: list[int], target: int) -> int | None:
    for i in range(len(values)):
        if values[i] == target:
            return i
    return None
