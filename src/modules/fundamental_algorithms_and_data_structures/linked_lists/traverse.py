from .linked_list_node import LinkedListNode


def traverse(head: LinkedListNode | None) -> list[int]:
    values = []
    current = head

    while current is not None:
        values.append(current.value)
        current = current.next

    return values
