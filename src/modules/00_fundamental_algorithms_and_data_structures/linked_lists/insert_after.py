from linked_lists.linked_list_node import LinkedListNode


def insert_after(node: LinkedListNode, value: int) -> None:
    """
    Insert a new node immediately after an existing node.

    The structure is modified by rewiring relationships rather than
    relocating existing nodes in memory.
    """
    new_node = LinkedListNode(next=node.next, value=value)
    node.next = new_node
