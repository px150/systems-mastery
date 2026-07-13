from linked_lists.linked_list_node import LinkedListNode
from linked_lists.traverse import traverse


def test_traverse_returns_values_in_linked_order():
    c = LinkedListNode(next=None, value=30)
    b = LinkedListNode(next=c, value=20)
    a = LinkedListNode(next=b, value=10)

    assert traverse(a) == [10, 20, 30]


def test_traverse_follows_links_not_creation_order():
    c = LinkedListNode(next=None, value=30)
    a = LinkedListNode(next=c, value=10)
    b = LinkedListNode(next=a, value=20)

    # La struttura è:
    #
    # b -> a -> c
    #
    # non:
    #
    # c -> a -> b

    assert traverse(b) == [20, 10, 30]


def test_traverse_single_node():
    node = LinkedListNode(next=None, value=10)

    assert traverse(node) == [10]


def test_traverse_empty_structure():
    assert traverse(None) == []
