from sort.merge_sort import merge, merge_sort


def test_merge_empty():
    assert merge([], []) == []


def test_merge_left_empty():
    assert merge([], [1, 3, 5]) == [1, 3, 5]


def test_merge_right_empty():
    assert merge([1, 3, 5], []) == [1, 3, 5]


def test_merge_sorted_lists():
    assert merge([1, 4, 8], [2, 3, 9]) == [1, 2, 3, 4, 8, 9]


def test_merge_left_exhausted_first():
    assert merge([1, 2], [3, 4, 5]) == [1, 2, 3, 4, 5]


def test_merge_right_exhausted_first():
    assert merge([4, 5], [1, 2, 3]) == [1, 2, 3, 4, 5]


def test_merge_duplicates():
    assert merge([1, 3, 3, 7], [2, 3, 5]) == [1, 2, 3, 3, 3, 5, 7]


def test_merge_negative_values():
    assert merge([-5, -1, 4], [-3, 0, 2]) == [-5, -3, -1, 0, 2, 4]


def test_merge_sort_empty():
    assert merge_sort([]) == []


def test_merge_sort_single_element():
    assert merge_sort([5]) == [5]


def test_merge_sort_two_elements():
    assert merge_sort([5, 2]) == [2, 5]


def test_merge_sort_unsorted():
    assert merge_sort([7, 3, 9, 2, 5]) == [2, 3, 5, 7, 9]


def test_merge_sort_even_number_of_elements():
    assert merge_sort([7, 3, 9, 2, 5, 8]) == [2, 3, 5, 7, 8, 9]


def test_merge_sort_already_sorted():
    assert merge_sort([2, 3, 5, 7, 9]) == [2, 3, 5, 7, 9]


def test_merge_sort_reverse_sorted():
    assert merge_sort([9, 7, 5, 3, 2]) == [2, 3, 5, 7, 9]


def test_merge_sort_duplicates():
    assert merge_sort([5, 2, 5, 3, 2]) == [2, 2, 3, 5, 5]


def test_merge_sort_all_equal():
    assert merge_sort([4, 4, 4, 4]) == [4, 4, 4, 4]


def test_merge_sort_negative_values():
    assert merge_sort([3, -2, 0, -7, 5]) == [-7, -2, 0, 3, 5]
