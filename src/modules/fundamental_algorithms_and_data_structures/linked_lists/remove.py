from linked_lists.linked_list_node import LinkedListNode


def remove(head: LinkedListNode | None, value: int) -> LinkedListNode | None:
    """
    Remove the first node containing the given value.

    Since singly linked structures do not store previous relationships,
    removal requires traversal from the head to locate the predecessor.

    Returns the (possibly updated) head of the structure.
    """
    current = head
    prev: LinkedListNode | None = None

    while current != None:
        if current.value == value:
            if prev is None:
                return current.next

            prev.next = current.next
            return head

        prev = current
        current = current.next

    return head
