from linked_lists.linked_list import LinkedList
from linked_lists.linked_list_node import LinkedListNode


def test_linked_list_starts_empty():
    linked_list = LinkedList()

    assert linked_list.head is None
    assert linked_list.traverse() == []


def test_linked_list_traverses_from_head():
    c = LinkedListNode(next=None, value=30)
    b = LinkedListNode(next=c, value=20)
    a = LinkedListNode(next=b, value=10)

    linked_list = LinkedList(head=a)

    assert linked_list.traverse() == [10, 20, 30]


def test_linked_list_remove_updates_head():
    b = LinkedListNode(next=None, value=20)
    a = LinkedListNode(next=b, value=10)

    linked_list = LinkedList(head=a)

    linked_list.remove(10)

    assert linked_list.head is b
    assert linked_list.traverse() == [20]


def test_linked_list_remove_middle_node():
    c = LinkedListNode(next=None, value=30)
    b = LinkedListNode(next=c, value=20)
    a = LinkedListNode(next=b, value=10)

    linked_list = LinkedList(head=a)

    linked_list.remove(20)

    assert linked_list.head is a
    assert linked_list.traverse() == [10, 30]


def test_linked_list_remove_missing_value_preserves_structure():
    b = LinkedListNode(next=None, value=20)
    a = LinkedListNode(next=b, value=10)

    linked_list = LinkedList(head=a)

    linked_list.remove(99)

    assert linked_list.head is a
    assert linked_list.traverse() == [10, 20]
