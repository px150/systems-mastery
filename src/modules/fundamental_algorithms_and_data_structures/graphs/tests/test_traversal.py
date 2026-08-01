from graphs.graph import Graph
from graphs.graph_node import GraphNode
from graphs.traversal import dfs_recursive, graph_traversal


def test_dfs_recursive_visits_every_node_once():
    graph = Graph()
    node1 = GraphNode(value=1)
    node2 = GraphNode(value=2)
    node3 = GraphNode(value=3)
    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_node(node3)
    graph.add_edge(node1, node2)
    graph.add_edge(node2, node3)
    graph.add_edge(node2, node1)
    assert dfs_recursive(node1) == [1, 2, 3]


def test_graph_traversal_visits_every_node_once():
    graph = Graph()
    node1 = GraphNode(value=1)
    node2 = GraphNode(value=2)
    node3 = GraphNode(value=3)
    node4 = GraphNode(value=4)
    node5 = GraphNode(value=5)
    graph.add_node(node1)
    graph.add_node(node2)
    graph.add_node(node3)
    graph.add_node(node4)
    graph.add_node(node5)
    graph.add_edge(node1, node2)
    graph.add_edge(node2, node3)
    graph.add_edge(node2, node1)
    graph.add_edge(node4, node5)
    graph.add_edge(node5, node4)
    assert graph_traversal(graph) == [1, 2, 3, 4, 5]
