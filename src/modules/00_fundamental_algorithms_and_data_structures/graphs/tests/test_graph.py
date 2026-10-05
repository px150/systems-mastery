import pytest

from graphs.graph import Graph, GraphNode


def test_add_already_present_node_to_graph():
    graph = Graph()
    node = GraphNode(value=1)
    graph.add_node(node)
    assert node in graph.nodes


def test_add_node_rejects_duplicate_node():
    graph = Graph()
    node = GraphNode(value=1)
    graph.add_node(node)
    with pytest.raises(ValueError, match="Node already in nodes."):
        graph.add_node(node)


def test_add_edge():
    graph = Graph()
    source = GraphNode(value=1)
    target = GraphNode(value=2)
    graph.add_node(source)
    graph.add_node(target)
    graph.add_edge(source, target)
    assert any(neighbor is target for neighbor in source.neighbors)


def test_add_edge_rejects_missing_source_node():
    graph = Graph()
    source = GraphNode(value=1)
    target = GraphNode(value=2)
    graph.add_node(target)
    with pytest.raises(ValueError, match="Source node is not in nodes."):
        graph.add_edge(source, target)


def test_add_edge_rejects_missing_target_node():
    graph = Graph()
    source = GraphNode(value=1)
    target = GraphNode(value=2)
    graph.add_node(source)
    with pytest.raises(ValueError, match="Target node is not in nodes."):
        graph.add_edge(source, target)


def test_add_edge_rejects_self_loop():
    graph = Graph()
    source = GraphNode(value=1)
    graph.add_node(source)
    with pytest.raises(ValueError, match="Source and target node are the same node."):
        graph.add_edge(source, source)


def test_add_edge_rejects_duplicate_edge():
    graph = Graph()
    source = GraphNode(value=1)
    target = GraphNode(value=2)
    graph.add_node(source)
    graph.add_node(target)
    graph.add_edge(source, target)
    with pytest.raises(ValueError, match="Edge between these nodes already exists."):
        graph.add_edge(source, target)


def test_add_edge_allows_opposite_direction():
    graph = Graph()
    source = GraphNode(value=1)
    target = GraphNode(value=2)

    graph.add_node(source)
    graph.add_node(target)

    graph.add_edge(source, target)
    graph.add_edge(target, source)

    assert any(neighbor is target for neighbor in source.neighbors)
    assert any(neighbor is source for neighbor in target.neighbors)


def test_add_edge_allows_distinct_nodes_with_same_value():
    graph = Graph()
    source = GraphNode(value=1)
    target = GraphNode(value=1)

    graph.add_node(source)
    graph.add_node(target)

    graph.add_edge(source, target)

    assert any(neighbor is target for neighbor in source.neighbors)
