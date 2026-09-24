def selection_sort(values: list[int]):
    for i in range(len(values) - 1):
        min_index = i
        for j in range(i, len(values)):
            if values[j] < values[min_index]:
                min_index = j
        values[i], values[min_index] = values[min_index], values[i]
