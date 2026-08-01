from graphs.graph import Graph
from graphs.graph_node import GraphNode
from graphs.dfs_recursive import dfs_recursive


def test_graph_dfs_recursive_visits_every_node_once():
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
