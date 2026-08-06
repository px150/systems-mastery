from hash_tables.hash_entry import HashEntry
from hash_tables.hash_table import HashTable


def test_hash_table_initializes_with_empty_independent_buckets():
    hash_table = HashTable()

    assert len(hash_table.buckets) == hash_table.capacity
    assert all(len(bucket) == 0 for bucket in hash_table.buckets)

    entry = HashEntry(key=0, value=0)
    hash_table.buckets[0].append(entry)

    assert hash_table.buckets[0] == [entry]
    assert all(len(bucket) == 0 for bucket in hash_table.buckets[1:])


def test_get_bucket_index_maps_key_within_capacity():
    hash_table = HashTable()
    index = hash_table._get_bucket_index(12345)
    assert 0 <= index < hash_table.capacity


def test_get_bucket_index_is_deterministic():
    hash_table = HashTable()
    key1 = hash_table._get_bucket_index(2)
    key2 = hash_table._get_bucket_index(2)
    assert key1 == key2 == 2


def test_get_bucket_index_allows_collisions():
    hash_table = HashTable()
    key1 = hash_table._get_bucket_index(2)
    key2 = hash_table._get_bucket_index(10)
    assert key1 == key2 == 2


def test_put_inserts_entry_into_empty_bucket():
    hash_table = HashTable()
    hash_table.put(8, 1)
    bucket = hash_table.buckets[0]
    assert bucket == [HashEntry(key=8, value=1)]


def test_put_updates_existing_key():
    hash_table = HashTable()
    hash_table.put(8, 1)
    hash_table.put(8, 2)
    bucket = hash_table.buckets[0]
    assert bucket == [HashEntry(key=8, value=2)]


def test_put_handles_collision():
    hash_table = HashTable()
    hash_table.put(8, 1)
    hash_table.put(16, 2)
    bucket = hash_table.buckets[0]
    assert bucket == [HashEntry(key=8, value=1), HashEntry(key=16, value=2)]


def test_put_increments_size_for_new_key():
    hash_table = HashTable()

    hash_table.put(8, 1)

    assert hash_table.size == 1


def test_put_does_not_increment_size_when_updating_existing_key():
    hash_table = HashTable()
    hash_table.put(8, 1)

    hash_table.put(8, 2)

    assert hash_table.size == 1


def test_get_returns_value_for_existing_key():
    hash_table = HashTable()
    hash_table.put(8, 1)

    assert hash_table.get(8) == 1


def test_get_returns_none_for_missing_key():
    hash_table = HashTable()

    assert hash_table.get(8) is None


def test_get_returns_correct_value_after_collision():
    hash_table = HashTable()
    hash_table.put(8, 1)
    hash_table.put(16, 2)

    assert hash_table.get(8) == 1
    assert hash_table.get(16) == 2


def test_load_factor_is_zero_for_empty_table():
    hash_table = HashTable()

    assert hash_table.load_factor == 0.0


def test_load_factor_reflects_size_and_capacity():
    hash_table = HashTable()
    hash_table.put(1, 10)
    hash_table.put(2, 20)

    assert hash_table.load_factor == 2 / hash_table.capacity


def test_should_rehash_returns_false_below_threshold():
    hash_table = HashTable()

    for i in range(6):
        hash_table.put(i, i)

    assert hash_table._should_rehash() is False


def test_rehash_doubles_capacity_and_preserves_all_entries():
    hash_table = HashTable()
    starting_capacity = hash_table.capacity
    for i in range(6):
        hash_table.put(i, i)
    size = hash_table.size
    hash_table.put(6, 6)
    assert hash_table.capacity == starting_capacity * 2
    assert hash_table.size == size + 1
    for i in range(7):
        assert hash_table.get(i) == i


def test_rehash_preserves_all_entries_after_bucket_changes():
    hash_table = HashTable()

    keys = [0, 8, 16, 24, 32, 40, 48]

    for key in keys:
        hash_table.put(key, key)

    assert hash_table.capacity == HashTable.DEFAULT_CAPACITY * 2

    for key in keys:
        assert hash_table.get(key) == key


def test_contains_returns_true_for_existing_key():
    hash_table = HashTable()
    hash_table.put(42, 100)

    assert hash_table.contains(42) is True


def test_contains_returns_false_for_missing_key():
    hash_table = HashTable()

    assert hash_table.contains(42) is False


def test_contains_handles_collision():
    hash_table = HashTable()
    hash_table.put(2, 100)
    hash_table.put(10, 200)

    assert hash_table.contains(2) is True
    assert hash_table.contains(10) is True
