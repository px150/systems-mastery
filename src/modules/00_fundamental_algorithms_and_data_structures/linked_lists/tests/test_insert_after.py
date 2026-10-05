from linked_lists.insert_after import insert_after
from linked_lists.linked_list_node import LinkedListNode
from linked_lists.traverse import traverse


def test_insert_after_adds_node_between_existing_nodes():
    c = LinkedListNode(next=None, value=30)
    b = LinkedListNode(next=c, value=20)
    a = LinkedListNode(next=b, value=10)

    insert_after(b, 25)

    assert traverse(a) == [10, 20, 25, 30]


def test_insert_after_adds_node_at_end():
    b = LinkedListNode(next=None, value=20)
    a = LinkedListNode(next=b, value=10)

    insert_after(b, 30)

    assert traverse(a) == [10, 20, 30]


def test_insert_after_preserves_existing_nodes():
    c = LinkedListNode(next=None, value=30)
    b = LinkedListNode(next=c, value=20)

    insert_after(b, 25)

    assert b.next.value == 25
    assert b.next.next is c
