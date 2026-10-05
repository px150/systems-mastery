def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    left_i = 0
    right_i = 0
    while left_i < len(left) and right_i < len(right):
        if left[left_i] <= right[right_i]:
            result.append(left[left_i])
            left_i += 1
        else:
            result.append(right[right_i])
            right_i += 1
    while left_i < len(left):
        result.append(left[left_i])
        left_i += 1
    while right_i < len(right):
        result.append(right[right_i])
        right_i += 1
    return result


def merge_sort(values: list[int]) -> list[int]:
    if len(values) <= 1:
        return values
    mid = len(values) // 2
    left = merge_sort(values[:mid])
    right = merge_sort(values[mid:])
    return merge(left, right)
