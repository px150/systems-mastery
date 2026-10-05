from collections import deque

from graphs.graph_node import GraphNode
from graphs.graph import Graph


def dfs_recursive(
    start_node: GraphNode,
    result: list[int] | None = None,
    visited: list[GraphNode] | None = None,
) -> list[int]:
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


def dfs_iterative(
    start_node: GraphNode,
) -> list[int]:
    result = []
    visited = []
    stack = [start_node]
    visited.append(start_node)
    while stack:
        current = stack.pop()
        result.append(current.value)
        for node in current.neighbors:
            if not any(visited_node is node for visited_node in visited):
                visited.append(node)
                stack.append(node)
    return result


def bfs_iterative(
    start_node: GraphNode,
) -> list[int]:
    result = []
    visited = []
    queue = deque([start_node])
    visited.append(start_node)
    while queue:
        current = queue.popleft()
        result.append(current.value)
        for node in current.neighbors:
            if not any(visited_node is node for visited_node in visited):
                visited.append(node)
                queue.append(node)
    return result


def graph_traversal(graph: Graph) -> list[int]:
    result = []
    visited = []
    for node in graph.nodes:
        if not any(visited_node is node for visited_node in visited):
            dfs_recursive(node, result, visited)
    return result
