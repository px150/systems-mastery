from linked_lists.linked_list_node import LinkedListNode
from linked_lists.remove import remove
from linked_lists.traverse import traverse


def test_remove_middle_node():
    c = LinkedListNode(next=None, value=30)
    b = LinkedListNode(next=c, value=20)
    a = LinkedListNode(next=b, value=10)

    head = remove(a, 20)

    assert traverse(head) == [10, 30]
    assert a.next is c


def test_remove_first_node_returns_new_head():
    c = LinkedListNode(next=None, value=30)
    b = LinkedListNode(next=c, value=20)
    a = LinkedListNode(next=b, value=10)

    head = remove(a, 10)

    assert head is b
    assert traverse(head) == [20, 30]


def test_remove_last_node():
    c = LinkedListNode(next=None, value=30)
    b = LinkedListNode(next=c, value=20)
    a = LinkedListNode(next=b, value=10)

    head = remove(a, 30)

    assert traverse(head) == [10, 20]
    assert b.next is None


def test_remove_only_node_returns_none():
    node = LinkedListNode(next=None, value=10)

    head = remove(node, 10)

    assert head is None
    assert traverse(head) == []


def test_remove_missing_value_preserves_structure():
    c = LinkedListNode(next=None, value=30)
    b = LinkedListNode(next=c, value=20)
    a = LinkedListNode(next=b, value=10)

    head = remove(a, 99)

    assert head is a
    assert traverse(head) == [10, 20, 30]


def test_remove_from_empty_structure_returns_none():
    head = remove(None, 10)

    assert head is None
