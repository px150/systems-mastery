from .linked_list_node import LinkedListNode


def traverse(head: LinkedListNode | None) -> list[int]:
    """
    Traverse a linked structure by following explicit relationships.

    Unlike arrays, elements are discovered through node-to-node traversal
    rather than direct address calculation.
    """
    values = []
    current = head

    while current is not None:
        values.append(current.value)
        current = current.next

    return values
