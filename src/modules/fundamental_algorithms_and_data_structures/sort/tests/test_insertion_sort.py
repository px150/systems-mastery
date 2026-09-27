from sort.insertion_sort import insertion_sort


def test_insertion_sort_empty():
    values = []

    insertion_sort(values)

    assert values == []


def test_insertion_sort_single_element():
    values = [5]

    insertion_sort(values)

    assert values == [5]


def test_insertion_sort_unsorted():
    values = [7, 3, 9, 2, 5]

    insertion_sort(values)

    assert values == [2, 3, 5, 7, 9]


def test_insertion_sort_already_sorted():
    values = [2, 3, 5, 7, 9]

    insertion_sort(values)

    assert values == [2, 3, 5, 7, 9]


def test_insertion_sort_reverse_sorted():
    values = [9, 7, 5, 3, 2]

    insertion_sort(values)

    assert values == [2, 3, 5, 7, 9]


def test_insertion_sort_duplicates():
    values = [5, 2, 5, 3, 2]

    insertion_sort(values)

    assert values == [2, 2, 3, 5, 5]


def test_insertion_sort_negative_values():
    values = [3, -2, 0, -7, 5]

    insertion_sort(values)

    assert values == [-7, -2, 0, 3, 5]
