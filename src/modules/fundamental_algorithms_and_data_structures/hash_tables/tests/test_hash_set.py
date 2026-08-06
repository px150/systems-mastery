from hash_tables.hash_set import HashSet


def test_add_inserts_element():
    hash_set = HashSet()

    hash_set.add(42)

    assert hash_set.contains(42) is True


def test_add_ignores_duplicate_elements():
    hash_set = HashSet()

    hash_set.add(42)
    hash_set.add(42)

    assert hash_set.size == 1


def test_contains_returns_false_for_missing_element():
    hash_set = HashSet()

    assert hash_set.contains(42) is False
