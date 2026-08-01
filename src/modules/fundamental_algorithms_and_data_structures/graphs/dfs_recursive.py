from graphs.graph_node import GraphNode


def dfs_recursive(
    start_node: GraphNode,
    result: list[int] | None = None,
    visited: list[GraphNode] | None = None,
):
    if result is None:
        result = []
    if visited is None:
        visited = []
    if any(node is start_node for node in visited):
        return result
    result.append(start_node.value)
    visited.append(start_node)
    for node in start_node.neighbors:
        dfs_recursive(node, result, visited)
    return result
