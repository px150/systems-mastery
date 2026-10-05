def binary_search(sorted_values: list[int], target: int) -> int | None:
    low = 0
    high = len(sorted_values) - 1
    while low <= high:
        mid = (high + low) // 2
        if sorted_values[mid] == target:
            return mid
        elif sorted_values[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None
