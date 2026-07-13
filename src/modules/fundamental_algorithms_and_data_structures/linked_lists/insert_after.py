from linked_lists.linked_list_node import LinkedListNode


def insert_after(node: LinkedListNode, value: int) -> None:
    new_node = LinkedListNode(next=node.next, value=value)
    node.next = new_node
