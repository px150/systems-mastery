from dataclasses import dataclass, field

from graphs.graph_node import GraphNode


@dataclass
class Graph:
    nodes: list[GraphNode] = field(default_factory=list)

    def add_node(self, node: GraphNode):
        for existing_node in self.nodes:
            if existing_node is node:
                raise ValueError("Node already in nodes.")
        self.nodes.append(node)

    def add_edge(self, source: GraphNode, target: GraphNode):
        if not any(existing_node is source for existing_node in self.nodes):
            raise ValueError("Source node is not in nodes.")
        if not any(existing_node is target for existing_node in self.nodes):
            raise ValueError("Target node is not in nodes.")
        if target is source:
            raise ValueError("Source and target node are the same node.")
        for existing_node in source.neighbors:
            if existing_node is target:
                raise ValueError("Edge between these nodes already exists.")
        source.neighbors.append(target)
